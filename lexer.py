# _*_ coding: utf-8 _*_
__author__ = 'daiyaquan'
__date__ = '2018/4/5 19:38'

from re import escape
from ply.lex import TOKEN

# 标识符
identify = ('NUMBER', 'ID')

# 保留字，TOKEN值为大写
reserved_list = ['true', 'false', 'print']
reserved = {s: s.upper() for s in reserved_list}

# 单字符的操作符 +-*/%><
operator_sg = {
    '+': 'ADD',
    '-': 'REM',
    '*': 'MUL',
    '/': 'DIV',
    '%': 'MOD',
    '<': 'LT',
    '>': 'GT',
    '(': 'LPAREN',
    ')': 'RPAREN',
}

"""
1. 配置tokens, 变量名必须为'tokens'
"""
tokens = list(identify) + list(reserved.values()) \
         + list(operator_sg.values())

"""
1. 为token配置规则
"""


# 数字的规则(只支持int类型)
def t_NUMBER(t):
    r'(0|[1-9]\d*)'
    t.value = int(t.value)
    return t


# 保留字和变量一起配置(官网推荐的做法)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check for reserved words, 如果是保留字，类型就是设置好的保留字类型，否则就是id类型
    t.type = reserved.get(t.value.lower(), 'ID')
    return t


# escape是将所有的字符自动转译成正则表达式能识别的字符
operator_sg_re = '[' + escape(''.join(operator_sg.keys())) + ']'
# 用装饰器将相应的正则表达式装载，原理是给__doc__赋值
@TOKEN(operator_sg_re)
def t_SPECIAL_MC(t):
    t.type = operator_sg.get(t.value, 'OPERATOR')
    return t


# 注释
def t_COMMENT(t):
    r'\#.*'


# 换行(用\n或者;)
def t_newline(t):
    r'\n+|;+'
    t.lexer.lineno += len(t.value)


# 先忽略空格和tab符
t_ignore = ' \t'


# lex出错时的反应
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)