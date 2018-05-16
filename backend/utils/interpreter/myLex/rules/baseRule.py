# _*_ coding: utf-8 _*_
__author__ = "dyq666"
__date__ = "2018/5/10 18:06"


"""
2.1 配置基础型的token
 - 默认情况下会将t_XXX的XXX作为对应的token的配置项
 - 比如token-NUMBER就对应t_NUMBER
 - 目前只支持 NUMBER, SPLIT
"""
# 数字的规则(只支持int类型)
def t_NUMBER(t):
    r'(0|[1-9]\d*)'
    t.value = int(t.value)
    return t

# 换行,同时也是语句的分隔符
def t_SPLIT(t):
    r'\n+'
    # 这里的t.value是\n组成的字符串, 一个\n代表应该增加一行
    t.lexer.lineno += len(t.value)
    return t


baseRulesObj = t_NUMBER, t_SPLIT
