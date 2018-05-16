# _*_ coding: utf-8 _*_
__author__ = "dyq666"
__date__ = "2018/5/10 18:41"

from interpreter.myExe.dexecute import DyqExecute

"""
1. 终结符是true false num string都是基础的赋值
2. 终结符是var时是action-get
"""

# true
def p_expression_true(p):
    'expression : TRUE'
    p[0] = True

# False
def p_expression_false(p):
    'expression : FALSE'
    p[0] = False

# 标识符NUMBER
def p_expression_num(p):
    'expression : NUMBER'
    p[0] = int(p[1])

# 标识符STRING
def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]

# 变量
def p_expression_var(p):
    'expression : VAR'
    p[0] = DyqExecute(action='get', params=[p[1]])


expressionEndRulesObj = p_expression_true, p_expression_false, p_expression_num, p_expression_string, p_expression_var
