class MyVarException(Exception):
    pass

class DyqExecute:
    res_string = []
    errors = []
    """
    1. 第一层, var_context, key: 作用域名 value: 作用域相关的属性
    2. 第二层, 作用域相关的属性, key: parent_field_name, var, value: 父作用域名, 该作用域下的变量
    """
    var_context = {
        'global': {
            'parent_field_name': None,
            'var': {}
        }
    }
    cur_field = 'global'
    field_name_index = 0

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
            'loop': self._loop,
            'assign_func': self._assign_func,
            'exe_func': self._exe_func
        }
        # 返回本次执行的结果
        result = action_dict.get(self.action, self._operation_error)()
        return result

    def _print(self):
        DyqExecute.res_string.append(' '.join(str(DyqExecute.resolve(x)) for x in list(self.params)))

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

    def _assign_func(self):
        # 2个参数就是无函数参数的, 3个参数就是有函数参数的
        if len(self.params) == 2:
            var_name, block_stmt_list = self.params
            self._resolve_save_var(var_name, block_stmt_list, DyqExecute.cur_field, is_func=True)
        # 如果是有函数参数就要进行特殊处理
        else:
            var_name, func_params, block_stmt_list = self.params
            self._resolve_save_var(var_name, block_stmt_list, DyqExecute.cur_field, True, func_params)

    def _exe_func(self):
        """
        1. params只有一个就是无函数参数的, params有两个参数就是有函数参数的
        2. 两种情况的第一个参数都是变量名
        """
        var = self.params[0]
        var_dict = self._get(var, is_func=True)
        if var_dict['type'] != 'func':
            raise MyVarException(f'{var} is not a function object')
        exe_list = var_dict['value']

        if len(self.params) == 1:
            # 获取执行列表, 并执行
            self._resolve_block(exe_list)

        else: # len(self.params) == 2
            # 获取函数实参数值并执行, 可能有一些简单的逻辑运算
            func_params = self.params[1]
            func_params = [DyqExecute.resolve(param) for param in func_params]

            # 获取函数定义时的参数名(形参)
            func_def_params = var_dict['params_name']

            if len(func_def_params) != len(func_params):
                raise MyVarException(f'function {var} params is error')

            # 形参与实参组合成函数的环境变量
            env_dict = {k: v for k, v in zip(func_def_params, func_params)}
            # 执行
            self._resolve_block(exe_list, unsaved_var=env_dict)

    def _condition(self):
        """
        1. params: [0(条件语句-交由logop执行), 1(一组待执行的实例)]
        """
        condition_is_true = DyqExecute.resolve(self.params[0])
        # 如果是true, 则执行所有实例
        if condition_is_true:
            self._resolve_block(self.params[1])
        # 也就是结果是false, 并且有else的语句(有三个参数)
        elif len(self.params) == 3:
            self._resolve_block(self.params[2])

    def _loop(self):
        """
        1. for-range循环
        2. params: [for循环中循环的变量名, 循环的数组, 一组待执行的实例]
        """
        for_var_name, for_array, exe_list = self.params
        # 遍历整个数组
        for num in for_array:
            # 将num存入对应的环境变量, 执行所有的实例
            self._resolve_block(exe_list, {for_var_name: num})

    def _triple_assign(self):
        """
        1. 三元赋值
        2. params: [var_name, condtion_expr, if_expr, else_expr]
        """
        # TODO 不能赋值已有的变量
        var_name, condtion_expr, if_expr, else_expr = self.params

        # 判断执行条件
        condition_is_true = DyqExecute.resolve(condtion_expr)
        # 获取变量值
        var_value = DyqExecute.resolve(if_expr) if condition_is_true else DyqExecute.resolve(else_expr)
        # 存入变量
        self._resolve_save_var(var_name, var_value, DyqExecute.cur_field)

    def _assign(self):
        """
        1. params: [0(变量名), 1(一个此类的实例)]
        """
        # 获取变量名
        var_name, exe_instance = self.params
        # 判断exe_instance是否是一个变量的名字
        obj = self._get(exe_instance.params[0], is_func=True, raise_error=False) if isinstance(exe_instance, DyqExecute) else None
        if obj is not None:
            # 是否为函数, 不是就是普通的变量
            if 'params_name' in obj:
                self._resolve_save_var(var_name, obj['value'], DyqExecute.cur_field, True, obj['params_name'])
            else:
                self._resolve_save_var(var_name, obj['value'], DyqExecute.cur_field)
        else:
            # 如果不是变量
            # 获取变量值
            var_value = DyqExecute.resolve(exe_instance)
            # 存入环境
            self._resolve_save_var(var_name, var_value, DyqExecute.cur_field)

    def _get(self, var=None, is_func=False, raise_error=True):
        """
        1. params: [0(变量名)]
        2. 从var_context获取值
        3. 成功则返回值
        4. 从所有父作用域获取变量失败则, 报错(如果raise_error为True), 返回None(为False)
        """
        var_name = self.params[0] if var is None else var

        # 当前搜索的作用域
        search_filed_name = DyqExecute.cur_field

        # 在当前环境下去获取值
        geted_var = DyqExecute.var_context[search_filed_name]['var'].get(var_name)
        # 如果找到了则返回值
        if geted_var is not None:
            # 如果是函数则返回整个var-dict
            if is_func:
                return geted_var
            return geted_var['value']

        # 如果没找到则改变作用域
        # 作用域变为父作用域
        search_filed_name = DyqExecute.var_context[search_filed_name]['parent_field_name']

        while search_filed_name is not None:
            # 从相应环境下获得值,
            geted_var = DyqExecute.var_context[search_filed_name]['var'].get(var_name)
            if geted_var is not None:
                if is_func:
                    return geted_var
                # 如果是函数则返回整个var-dict
                return geted_var['value']
            search_filed_name = DyqExecute.var_context[search_filed_name]['parent_field_name']
        # 如果所有父作用域都没有
        else:
            if raise_error:
                raise MyVarException(f'{var_name} is not exist')
            else:
                return None

    def _resolve_block(self, exe_list, unsaved_var=None):
        # 创建一个新的环境, 并且切换环境
        DyqExecute._add_change_field()

        # 如果有未存入环境的变量
        if unsaved_var:
            for var_name, var_value in unsaved_var.items():
                self._resolve_save_var(var_name, var_value, DyqExecute.cur_field)

        # 执行所有实例
        for single_exe in exe_list:
            DyqExecute.resolve(single_exe)

        # 将环境变为父环境(global没有父环境)
        parent_field_name = DyqExecute.var_context[DyqExecute.cur_field]['parent_field_name']
        if parent_field_name is not None:
            DyqExecute.cur_field = DyqExecute.var_context[DyqExecute.cur_field]['parent_field_name']

    def _resolve_save_var(self, var_name, var_value, field_name='global', is_func=False, params_name=None):
        """根据作用域存储变量"""
        # 获取作用域, 如果没有则生成新的作用域
        field = DyqExecute.var_context[field_name]
        # 在对应的作用域的key(var)中存储值
        field['var'][var_name] = {
            'value': var_value
        }

        # 如果是函数则将参数名存入变量
        if is_func:
            if params_name is not None:
                field['var'][var_name]['params_name'] = params_name
            field['var'][var_name]['type'] = 'func'
        else:
            field['var'][var_name]['type'] = 'var'

    @classmethod
    def _add_change_field(cls):
        # 记录当前的环境作为新环境的父环境
        parent_field_name = DyqExecute.cur_field
        # 获取一个新环境, 并将当前环境变成新环境
        cur_field_name = DyqExecute.getFieldName()
        DyqExecute.cur_field = cur_field_name

        # 生成新的作用域
        DyqExecute.var_context[cur_field_name] = {
            'parent_field_name': parent_field_name,
            'var': {}
        }

    @classmethod
    def getFieldName(cls):
        """返回一个新的作用域名"""
        DyqExecute.field_name_index += 1
        return 'field' + str(DyqExecute.field_name_index)

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
