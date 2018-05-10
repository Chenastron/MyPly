# _*_ coding: utf-8 _*_
__author__ = "dyq666"
__date__ = "2018/5/10 18:18"

from re import escape
from ply.lex import TOKEN

from ..settings import settingsObj

states, identify, reserved, operator_single, operator_double = settingsObj

# 双字符的操作符要放在单字符操作符上面，优先匹配
operator_double_re = '(' + '|'.join(escape(x) for x in operator_double.keys()) + ')'
# 用装饰器将相应的正则表达式装载，原理是给__doc__赋值
@TOKEN(operator_double_re)
def t_OPERATOR_DOUBLE(t):
    t.type = operator_double.get(t.value, 'OPERATER_DOUBLE')
    return t


# escape是将所有的字符自动转译成正则表达式能识别的字符
operator_single_re = '[' + escape(''.join(operator_single.keys())) + ']'
# 用装饰器将相应的正则表达式装载，原理是给__doc__赋值
@TOKEN(operator_single_re)
def t_OPERATOR_SINGLE(t):
    t.type = operator_single.get(t.value, 'OPERATOR_SINGLE')
    return t


operatorRulesObj = t_OPERATOR_DOUBLE, t_OPERATOR_SINGLE
