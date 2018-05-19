# _*_ coding: utf-8 _*_
__author__ = "dyq666"
__date__ = "2018/5/10 17:16"


# 状态控制
states = (
    ('string', 'inclusive'),
)

"""
这里indentify配置的都是token
"""
# 标识符
identify = ('NUMBER', 'VAR', 'STRING', 'SPLIT')


"""
这里配置的全是字典
value: token
key: 
"""
# 保留字，TOKEN值为大写
reserved_list = ['true', 'false', 'print', 'and', 'or', 'if', 'else', 'for', 'in', 'range', 'func']
reserved = {s: s.upper() for s in reserved_list}

# 单字符的操作符 +-*/% <> () = ,:
operator_single = {
    '+': 'ADD',
    '-': 'REM',
    '*': 'MUL',
    '/': 'DIV',
    '%': 'MOD',
    '<': 'LT',
    '>': 'GT',
    '(': 'LPAREN',
    ')': 'RPAREN',
    '=': 'ASSIGN',
    ',': 'COMMA',
    '{': 'START_BLOCK',
    '}': 'END_BLOCK'
}

# 双字符的操作符 >= <= == != **
operator_double = {
    '>=': 'GE',
    '<=': 'LE',
    '==': 'EQ',
    '!=': 'NE',
    '**': 'POW',
}

settingsObj = (states, identify, reserved, operator_single, operator_double)
