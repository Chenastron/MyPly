# _*_ coding: utf-8 _*_
__author__ = "dyq666"
__date__ = "2018/5/10 18:09"

"""
2.2 配置需要用到state(状态)的token
 - STRING也是用t_xxx的形式
"""
# 字符串起始位置
def t_STRING(t):
    r'["\']'
    t.lexer.begin('string')
    t.lexer.str_start = t.lexer.lexpos
    t.lexer.str_marker = t.value
# 忽略所有以"'开头的字符, 也就是字符串的主体
def t_string_content(t):
    r'[^"\']+'
# 字符串结束为止
def t_string_end(t):
    r'["\']'
    if t.lexer.str_marker == t.value:
        t.type = 'STRING'
        t.value = t.lexer.lexdata[t.lexer.str_start:t.lexer.lexpos - 1]
        # 默认的状态是initial
        t.lexer.begin('INITIAL')
        return t


stringRuleObj = t_STRING, t_string_content, t_string_end
