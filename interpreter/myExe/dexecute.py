class DyqExecute:
    res_string = []
    has_error = False
    errors = []
    var_context = {}

    def __init__(self, action=None, params=None):
        self.action = action
        self.params = params

    def execute(self):
        """执行"""
        action_dict = {
            'print': self._print,
            'assign': self._assign,
            'triple_assign': self._triple_assign,
            'get': self._get,
            'condition': self._condition,
            'logop': self._logop,
            'binop': self._binop,
            'loop': self._loop
        }
        # 返回本次执行的结果
        result = action_dict.get(self.action, self._operation_error)()
        return result

    def _print(self):
        DyqExecute.res_string.append(' '.join(str(DyqExecute.resolve(x)) for x in list(self.params)))

    def _condition(self):
        """
        1. params: [0(条件语句-交由logop执行), 1(一组待执行的实例)]
        """
        condition_is_true = DyqExecute.resolve(self.params[0])
        # 如果是true, 则执行所有实例
        if condition_is_true:
            for single_exe in self.params[1]:
                DyqExecute.resolve(single_exe)

    def _loop(self):
        for i in self.params[1]:
            DyqExecute.var_context[self.params[0]] = i
            DyqExecute.resolve(self.params[2])

    def _logop(self):
        params = list(self.params)
        result = DyqExecute.resolve(params.pop())
        while len(params) >= 2:
            prev = result
            op = DyqExecute.resolve(params.pop()).upper()
            comp = DyqExecute.resolve(params.pop())
            result = {
                'AND': lambda a, b: (a and b),
                'OR': lambda a, b: (a or b),
            }[op](prev, comp)
        return result

    def _binop(self):

        """
        1. 二元运算
        2. params: [0(左执行实例), 1(操作符), 2(右执行实例)]
        """
        a = DyqExecute.resolve(self.params[0])
        b = DyqExecute.resolve(self.params[2])
        op = self.params[1]
        result = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
            '%': lambda a, b: a % b,
            '**': lambda a, b: a ** b,
            '>': lambda a, b: (a > b),
            '>=': lambda a, b: (a >= b),
            '<': lambda a, b: (a < b),
            '<=': lambda a, b: (a <= b),
            '==': lambda a, b: (a == b),
            '!=': lambda a, b: (a != b),
        }[op](a, b)
        return result

    def _triple_assign(self):
        """
        1. 三元赋值
        2. params: [var_name, condtion_expr, if_expr, else_expr]
        """
        var_name, condtion_expr, if_expr, else_expr = self.params

        # 判断执行条件
        condition_is_true = DyqExecute.resolve(condtion_expr)
        # 获取变量值
        var_value = DyqExecute.resolve(if_expr) if condition_is_true else DyqExecute.resolve(else_expr)
        # 存入变量
        DyqExecute.var_context[var_name] = var_value


    def _assign(self):
        """
        1. params: [0(变量名), 1(一个此类的实例)]
        """
        # 获取变量名
        var_name, exe_instance = self.params
        # 获取变量值
        var_value = DyqExecute.resolve(exe_instance)
        # 存入环境
        DyqExecute.var_context[var_name] = var_value

    def _get(self):
        """
        1. params: [0(变量名)]
        2. 从var_context获取值
        3. 成功则返回值
        4. 失败则报错
        """
        var_name = self.params[0]
        geted_var = DyqExecute.var_context.get(var_name)

        # 变量名不存在(None)则停止运行
        if geted_var is None:
            DyqExecute.has_error = True
            DyqExecute.errors.append(f'[VAR_ERROR]: {var_name} is not exist')
        # 变量名存在则返回对应的值
        else:
            return geted_var

    @staticmethod
    def isDyqExecuteObj(obj=None):
        """判断是否是这个类的实例"""
        return obj is not None and isinstance(obj, DyqExecute)

    @staticmethod
    def resolve(x):
        """如果是这个类的实例则执行"""
        return x.execute() if DyqExecute.isDyqExecuteObj(x) else x

    def __str__(self):
        return '[DEXE] %s %s' % (self.action, ';'.join(str(x) for x in self.params))

    def _operation_error(self):
        """判断是否支持这个操作"""
        print("Error, unsupported operation:", str(self))
