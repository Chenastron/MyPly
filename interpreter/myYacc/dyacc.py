from interpreter.myLex.dlexer import tokens
from interpreter.myExe.dexecute import DyqExecute

from .settings import settingObj
from .rules.expressionEndRule import expressionEndRulesObj

exelist = []

# 读取配置, 目前只有优先级
precedence, *_ = settingObj


def p_entry(p):
    'entry : start'
    # p[0] = p[1]
    p[0] = exelist


def p_start(p):
    '''
    start : start stmt_print SPLIT
             | start stmt
             | empty
    '''
    if len(p) > 2:
        exelist.append(p[2])
        p[0] = p[2]


def p_stmt_print_none(p):
    'stmt : SPLIT'


def p_stmt_print_expr(p):
    'stmt : expression SPLIT'
    p[0] = p[1]


"""print语句"""
def p_stmt_print_print(p):
    '''
    stmt_print : PRINT LPAREN expr_list RPAREN
    '''
    p[0] = DyqExecute(action='print', params=p[3])
def p_expression_list(p):
    '''
    expr_list : expression
              | expr_list COMMA expression
    '''
    if len(p) <= 3:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


"""两条语法for循环的语句"""
def p_range(p):
    'range : RANGE LPAREN expr_list RPAREN'
    p[0] = list(range(p[3][0], p[3][1]))
def p_stmt_print_for(p):
    'stmt : FOR VAR IN range COLON stmt_print SPLIT'
    p[0] = DyqExecute(action='loop', params=[p[2], p[4], p[6]])


"""两条语法为三元表达式赋值的语句"""
def p_stmt_print_cond_postfix_assign(p):
    'stmt : if_assign IF condition_list ELSE expression SPLIT'
    p[0] = DyqExecute(action='assign', params=[
        p[1][0], DyqExecute(action='condition', params=[p[3], p[1][1], p[5]])
    ])
def p_ifassign(p):
    'if_assign : VAR ASSIGN expression'
    p[0] = [p[1], p[3]]


"""if语句"""
def p_stmt_print_cond(p):
    '''
    stmt : IF condition_list COLON stmt_print SPLIT
         | IF condition_list COLON SPLIT stmt_print SPLIT
    '''
    # 分为上面两种情况，一个stmt的位置在4,一个在5(0开始计数)
    if len(p) < 7:
        p[0] = DyqExecute(action='condition', params=[p[2], p[4]])
    else:
        p[0] = DyqExecute(action='condition', params=[p[2], p[5]])


"""if-block语句"""
def p_stmt_if_block(p):
    '''
    stmt : IF condition_list START_BLOCK SPLIT stmt_print SPLIT END_BLOCK SPLIT
    '''
    p[0] = DyqExecute(action='condition', params=[p[2], p[5]])


"""赋值语句"""
def p_stmt_assign(p):
    '''
    stmt : VAR ASSIGN expression SPLIT
         | VAR ASSIGN condition_list SPLIT
    '''
    p[0] = DyqExecute(action='assign', params=[p[1], p[3]])


"""下面开始是表达式"""

# 逻辑控制语句(少一个优先级)
def p_condition_list(p):
    '''
    condition_list : expression
                   | condition_list AND expression
                   | condition_list OR expression
    '''

    if len(p) > 2:
        p[0] = DyqExecute(action='logop', params=p[1:])
    else:
        p[0] = p[1]


# 增加括号(控制语句)功能
def p_condition_parens(p):
    'condition_list : LPAREN condition_list RPAREN'
    p[0] = p[2]


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


# 表达式: 终结符的语法
p_expression_true, p_expression_false, p_expression_num, p_expression_string, p_expression_var = expressionEndRulesObj


"""
非语法配置
"""
# 出错
def p_error(p):
    print("Syntax error in input!", p)
# 必须品
def p_empty(p):
    'empty :'

def debug(*params):
    print("[DBG] %s" % (' : '.join(str(x) for x in params),))