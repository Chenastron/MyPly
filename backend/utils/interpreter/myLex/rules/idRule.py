# _*_ coding: utf-8 _*_
__author__ = "dyq666"
__date__ = "2018/5/10 18:13"

"""
2.3 配置
 - 配置变量和保留字
 - 先判断是否为保留字, 是则将type变成对应的TOKEN, 否则就是变量
"""

from ..settings import settingsObj
states, identify, reserved, operator_single, operator_double = settingsObj

# 保留字和变量一起配置(官网推荐的做法)
def t_VAR_RESERVED(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check for reserved words, 如果是保留字，类型就是设置好的保留字类型，否则就是id类型
    t.type = reserved.get(t.value, 'VAR')
    return t


idRuleObj = t_VAR_RESERVED
