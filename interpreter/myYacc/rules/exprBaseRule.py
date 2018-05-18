# _*_ coding: utf-8 _*_
__author__ = "dyq666"
__date__ = "2018/5/18 11:30"

from interpreter.myExe.dexecute import DyqExecute

# 二元操作符
def p_expression_two_operator(p):
    '''
    expression : expression ADD expression
               | expression REM expression
               | expression MUL expression
               | expression DIV expression
               | expression MOD expression
               | expression GT expression
               | expression LT expression
               | expression GE expression
               | expression LE expression
               | expression EQ expression
               | expression NE expression
               | expression POW expression
    '''
    p[0] = DyqExecute(action='binop', params=p[1:])


# 增加括号(表达式)功能
def p_expression_parens(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


exprBaseRulesObj = p_expression_two_operator, p_expression_parens
