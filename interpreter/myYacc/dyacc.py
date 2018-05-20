from interpreter.myLex.dlexer import tokens
from interpreter.myExe.dexecute import DyqExecute

from .settings import settingObj

exelist = []

# 读取配置, 目前只有优先级
precedence, *_ = settingObj


def p_entry(p):
    'entry : start'
    # p[0] = p[1]
    p[0] = exelist


def p_start(p):
    '''
    start : start stmt
          | empty
    '''
    if len(p) > 2:
        exelist.append(p[2])
        p[0] = p[2]


def p_stmt_none(p):
    'stmt : SPLIT'


def p_stmt_expr(p):
    'stmt : expression SPLIT'
    p[0] = p[1]

"""函数语句"""
def p_stmt_func_define_non_params(p):
    '''
    stmt : VAR ASSIGN LPAREN RPAREN block_format
    '''
    var_name, block_stmt_list = p[1], p[5]
    p[0] = DyqExecute(action='assign_func', params=[
        var_name, block_stmt_list
    ])

def p_stmt_func_define_non_params_func(p):
    '''
    stmt : FUNC VAR LPAREN RPAREN block_format
    '''
    var_name, block_stmt_list = p[2], p[5]
    p[0] = DyqExecute(action='assign_func', params=[
        var_name, block_stmt_list
    ])

def p_stmt_func_define_params(p):
    '''
    stmt : VAR ASSIGN LPAREN func_params RPAREN block_format
    '''
    var_name, func_params, block_stmt_list = p[1], p[4], p[6]
    p[0] = DyqExecute(action='assign_func', params=[
        var_name, func_params, block_stmt_list
    ])

def p_stmt_func_define_params_func(p):
    '''
    stmt : FUNC VAR LPAREN func_params RPAREN block_format
    '''
    var_name, func_params, block_stmt_list = p[2], p[4], p[6]
    p[0] = DyqExecute(action='assign_func', params=[
        var_name, func_params, block_stmt_list
    ])

def p_func_params_list(p):
    '''
    func_params : VAR
                | func_params COMMA VAR
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_stmt_func_exe_non_params(p):
    '''
    stmt : VAR LPAREN RPAREN SPLIT
    '''
    p[0] = DyqExecute(action='exe_func', params=[p[1]])

def p_stmt_func_exe_params(p):
    '''
    stmt : VAR LPAREN expr_list RPAREN SPLIT
    '''
    p[0] = DyqExecute(action='exe_func', params=[p[1], p[3]])

"""print语句"""
def p_stmt_print(p):
    '''
    stmt : PRINT LPAREN expr_list RPAREN SPLIT
    '''
    p[0] = DyqExecute(action='print', params=p[3])


"""两条语法for循环的语句"""
def p_stmt_for(p):
    'stmt : FOR VAR IN range block_format'
    for_var_name = p[2]
    for_range = p[4]
    block_stmt_list = p[5]
    p[0] = DyqExecute(action='loop', params=[
        for_var_name, for_range, block_stmt_list
    ])
def p_range(p):
    'range : RANGE LPAREN expr_list RPAREN'
    p[0] = list(range(p[3][0], p[3][1], p[3][2]))


"""if语句"""
def p_stmt_if_block(p):
    '''
    stmt : IF condition_list block_format
         | IF condition_list block_format ELSE block_format
    '''
    if len(p) == 4:
        p[0] = DyqExecute(action='condition', params=[p[2], p[3]])
    else:
        p[0] = DyqExecute(action='condition', params=[p[2], p[3], p[5]])


"""语句块, 分别为控制block的样式, block真正代表的语句块"""
def p_block_format(p):
    '''
    block_format : START_BLOCK SPLIT block END_BLOCK SPLIT
    '''
    p[0] = p[3]
def p_block(p):
    '''
    block : stmt
          | block stmt
    '''
    # [第一条语句, 第二条语句, ···, 最后一条语句]
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


"""赋值语句"""
def p_stmt_assign(p):
    '''
    stmt : VAR ASSIGN expression SPLIT
         | VAR ASSIGN condition_list SPLIT
    '''
    p[0] = DyqExecute(action='assign', params=[p[1], p[3]])


"""两条语法为三元表达式赋值的语句"""
def p_stmt_triple_assign(p):
    'stmt : if_assign IF condition_list ELSE expression SPLIT'
    var_name = p[1][0]
    condtion_expr = p[3]
    if_expr = p[1][1]
    else_expr = p[5]
    p[0] = DyqExecute(action='triple_assign', params=[
        var_name, condtion_expr, if_expr, else_expr
    ])
def p_ifassign(p):
    'if_assign : VAR ASSIGN expression'
    p[0] = [p[1], p[3]]


"""
--------------------
下面开始是表达式
"""
# 用逗号分隔的多表达式
def p_expression_list(p):
    '''
    expr_list : expression
              | expr_list COMMA expression
    '''
    if len(p) <= 3:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


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

# 负数
def p_negative_number(p):
    'expression : REM NUMBER'
    p[0] = -p[2]

# 增加括号(表达式)功能
def p_expression_parens(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


# true
def p_expression_true(p):
    'expression : TRUE'
    p[0] = True

# False
def p_expression_false(p):
    'expression : FALSE'
    p[0] = False

# 标识符NUMBER
def p_expression_num(p):
    'expression : NUMBER'
    p[0] = int(p[1])

# 标识符STRING
def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]

# 变量
def p_expression_var(p):
    'expression : VAR'
    p[0] = DyqExecute(action='get', params=[p[1]])


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
