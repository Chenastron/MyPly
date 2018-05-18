var_context = {}


class DyqExecute:
    res_string = []

    def __init__(self, action=None, params=None):
        self.action = action
        self.params = params
        DyqExecute.res_string = []

    def execute(self):
        """执行"""
        action_dict = {
            'print': self._print,
            'assign': self._assign,
            'get': self._get,
            'condition': self._condition,
            'logop': self._logop,
            'binop': self._binop,
            'loop': self._loop,
        }
        # 返回本次执行的结果
        result = action_dict.get(self.action, self._operation_error)()
        return result

    def _print(self):
        DyqExecute.res_string.append(' '.join(str(DyqExecute.resolve(x)) for x in list(self.params)))

    def _assign(self):
        result = var_context[self.params[0]] = DyqExecute.resolve(self.params[1])
        return result

    def _get(self):
        result = var_context.get(self.params[0], 0)
        return result

    def _condition(self):
        result = None
        if DyqExecute.resolve(self.params[0]):
            result = DyqExecute.resolve(self.params[1])
        # 如果失败了则执行else后面的参数
        elif len(self.params) > 2:
            result = DyqExecute.resolve(self.params[2])
        return result

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

    def _loop(self):
        for i in self.params[1]:
            var_context[self.params[0]] = i
            DyqExecute.resolve(self.params[2])

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