# _*_ coding: utf-8 _*_
__author__ = 'daiyaquan'
__date__ = '2018/4/5 19:37'


from ply import lex, yacc

from interpreter.myLex import dlexer
from interpreter.myYacc import dparser
from interpreter.myExe.dexecute import DyqExecute

# 读入词法分析器和语法分析器
lexs = lex.lex(module=dlexer)
parses = yacc.yacc(module=dparser)


def show_lex():
    """显示词法分析器的结果"""
    lexs.input(data)
    for l in lexs:
        print(l)


def show_parse():
    """显示语法分析器的结果"""
    for x in parses.parse(data):
        print(x)


def show_exe():
    """显示最终执行的结果"""
    for x in parses.parse(data):
        DyqExecute.resolve(x)

file_choice = 2
file_path = 'sub_test' if file_choice == 1 else 'test_code.py'
# 读入要执行的代码
with open(file_path, 'r') as f:
    data = f.read()


show_dict = {
    1: show_lex,
    2: show_parse,
    3: show_exe
}

choice = 2
show_dict[choice]()
