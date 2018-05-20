# _*_ coding: utf-8 _*_
__author__ = "dyq666"
__date__ = "2018/5/10 19:25"


from ply import lex, yacc

from interpreter.myLex import dlexer
from interpreter.myYacc import dyacc
from interpreter.myExe.dexecute import DyqExecute, MyVarException


class OutputRes:
    """
    1. 外界使用这个module仅需要声明这个类的实例
    2. 创建实例时传入一个待解析的字符串
    3. 使用实例方法get_Res()得到结果, 结果为一个dict三个key分别为‘lex’ ‘yacc' 'exe'
    """
    def __init__(self, data):
        # 读入词法分析器和语法分析器
        self.lexor = lex.lex(module=dlexer)
        self.yaccor = yacc.yacc(module=dyacc)
        # 读入要被解析的字符串
        # 如果最后没有最后空的一行则加上空的一行
        # self.data = data if data[-1] == '\n' else data + '\n'
        self.data = data + '\n'

    def _evaluate_lex(self):
        """计算词法分析器的结果"""
        self.lexor.input(self.data)
        return '\n'.join([str(single_lex) for single_lex in self.lexor])

    def _evaluate_yacc(self):
        """计算语法分析器的结果"""
        # 重置语法分析结果
        dyacc.exelist = []
        return '\n'.join([str(single_yacc) for single_yacc in self.yaccor.parse(self.data, lexer=self.lexor)])

    def _evaluate_exe(self):
        """计算最终执行的结果"""
        # 重置语法分析结果
        dyacc.exelist = []
        DyqExecute.res_string = []
        DyqExecute.errors = []
        for x in self.yaccor.parse(self.data, lexer=self.lexor):
            # 如果执行没有报错则再继续执行
            try:
                DyqExecute.resolve(x)
            except MyVarException as e:
                # 报错后将错误信息存入, 取消之后的执行
                DyqExecute.errors.append('[EXE_ERROR]' + str(e))
                break

        # 将所有错误信息与结果信息相加
        res = DyqExecute.res_string + DyqExecute.errors
        # 将结果变成字符串返回
        return '\n'.join(res)

    def get_res(self):
        """返回结果"""
        # 将之前保存语法分析器的数据重置为空
        return {
            'lex': self._evaluate_lex(),
            'yacc': self._evaluate_yacc(),
            'exe': self._evaluate_exe()
        }
