# _*_ coding: utf-8 _*_
__author__ = 'daiyaquan'
__date__ = '2018/4/5 19:38'

from .settings import settingsObj
from .rules.baseRule import baseRulesObj
from .rules.stringRule import stringRuleObj
from .rules.idRule import idRuleObj
from .rules.operatorRule import operatorRulesObj

# 从配置中获取状态配置, token配置, 部分token对应的正则配置
states, identify, reserved, operator_single, operator_double = settingsObj

"""
1. 配置tokens, 变量名必须为'tokens'
"""
tokens = list(identify) + list(reserved.values()) + \
         list(operator_single.values()) + list(operator_double.values())

"""
2. 为token配置规则 
"""
# 配置基础型token的规则
t_FLOAT, t_NUMBER, t_SPLIT = baseRulesObj
# 配置string的token规则
t_STRING, t_string_content, t_string_end = stringRuleObj
# 配置var和reserved的token规则
t_VAR_RESERVED = idRuleObj
t_OPERATOR_DOUBLE, t_OPERATOR_SINGLE = operatorRulesObj


"""
3. 为非token配置规则
"""
# 注释
def t_COMMENT(t):
    r'\#.*'
# 先忽略空格和tab符
t_ignore = ' \t'
# lex出错时的反应
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
