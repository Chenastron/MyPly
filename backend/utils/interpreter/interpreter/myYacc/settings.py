# _*_ coding: utf-8 _*_
__author__ = "dyq666"
__date__ = "2018/5/10 18:31"

precedence = (
    # ('nonassoc', 'IFX', 'SPLIT'),
    # ('left', 'CONDLIST'),
    ('left', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE'),
    ('left', 'REM', 'ADD'),
    ('left', 'MUL', 'DIV', 'MOD'),
    ('left', 'POW'),
)


settingObj = (precedence,)
