
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftLTLEGTGEEQNEleftREMADDleftMULDIVMODleftPOWADD AND ASSIGN COMMA DIV ELSE END_BLOCK EQ FALSE FOR FUNC GE GT IF IN LE LPAREN LT MOD MUL NE NUMBER OR POW PRINT RANGE REM RPAREN SPLIT START_BLOCK STRING TRUE VARentry : startexpression : TRUEexpression : FALSE\n    start : start stmt\n          | empty\n    expression : NUMBERexpression : STRINGstmt : SPLITstmt : expression SPLITexpression : VAR\n    stmt : VAR ASSIGN LPAREN RPAREN block_format\n    \n    stmt : VAR ASSIGN LPAREN func_params RPAREN block_format\n    \n    func_params : VAR\n                | func_params COMMA VAR\n    \n    stmt : VAR LPAREN RPAREN SPLIT\n    \n    stmt : VAR LPAREN expr_list RPAREN SPLIT\n    \n    stmt : PRINT LPAREN expr_list RPAREN SPLIT\n    stmt : FOR VAR IN range block_formatrange : RANGE LPAREN expr_list RPAREN\n    stmt : IF condition_list block_format\n    \n    block_format : START_BLOCK SPLIT block END_BLOCK SPLIT\n    \n    block : stmt\n          | block stmt\n    \n    stmt : VAR ASSIGN expression SPLIT\n         | VAR ASSIGN condition_list SPLIT\n    stmt : if_assign IF condition_list ELSE expression SPLITif_assign : VAR ASSIGN expression\n    expr_list : expression\n              | expr_list COMMA expression\n    \n    condition_list : expression\n                   | condition_list AND expression\n                   | condition_list OR expression\n    condition_list : LPAREN condition_list RPAREN\n    expression : expression ADD expression\n               | expression REM expression\n               | expression MUL expression\n               | expression DIV expression\n               | expression MOD expression\n               | expression GT expression\n               | expression LT expression\n               | expression GE expression\n               | expression LE expression\n               | expression EQ expression\n               | expression NE expression\n               | expression POW expression\n    expression : LPAREN expression RPARENempty :'
    
_lr_action_items = {'SPLIT':([0,2,3,4,5,6,7,13,14,15,16,17,33,40,41,42,43,44,45,46,47,48,49,50,51,53,54,55,58,61,64,73,74,75,76,78,81,82,83,84,86,89,91,92,94,95,96,97,100,101,102,104,],[-47,5,-5,-4,-8,17,-10,-2,-3,-6,-7,-9,-10,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,73,74,75,-46,-20,83,-24,-25,-15,89,91,-31,-32,5,-33,-11,-16,-17,-18,5,-22,102,-12,104,-23,-26,-21,]),'VAR':([0,2,3,4,5,8,10,11,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,38,39,52,61,62,63,69,73,74,75,77,83,85,86,88,89,91,92,93,94,95,97,101,102,104,],[-47,7,-5,-4,-8,33,35,33,-9,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,68,-20,33,33,33,-24,-25,-15,33,7,33,-11,98,-16,-17,-18,33,7,-22,-12,-23,-26,-21,]),'PRINT':([0,2,3,4,5,17,61,73,74,75,83,86,89,91,92,94,95,97,101,102,104,],[-47,9,-5,-4,-8,-9,-20,-24,-25,-15,9,-11,-16,-17,-18,9,-22,-12,-23,-26,-21,]),'FOR':([0,2,3,4,5,17,61,73,74,75,83,86,89,91,92,94,95,97,101,102,104,],[-47,10,-5,-4,-8,-9,-20,-24,-25,-15,10,-11,-16,-17,-18,10,-22,-12,-23,-26,-21,]),'IF':([0,2,3,4,5,12,13,14,15,16,17,33,40,41,42,43,44,45,46,47,48,49,50,51,53,58,61,73,74,75,83,86,89,91,92,94,95,97,101,102,104,],[-47,11,-5,-4,-8,39,-2,-3,-6,-7,-9,-10,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-27,-46,-20,-24,-25,-15,11,-11,-16,-17,-18,11,-22,-12,-23,-26,-21,]),'TRUE':([0,2,3,4,5,8,11,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,38,39,52,61,62,63,69,73,74,75,77,83,85,86,89,91,92,93,94,95,97,101,102,104,],[-47,13,-5,-4,-8,13,13,-9,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,-20,13,13,13,-24,-25,-15,13,13,13,-11,-16,-17,-18,13,13,-22,-12,-23,-26,-21,]),'FALSE':([0,2,3,4,5,8,11,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,38,39,52,61,62,63,69,73,74,75,77,83,85,86,89,91,92,93,94,95,97,101,102,104,],[-47,14,-5,-4,-8,14,14,-9,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-20,14,14,14,-24,-25,-15,14,14,14,-11,-16,-17,-18,14,14,-22,-12,-23,-26,-21,]),'NUMBER':([0,2,3,4,5,8,11,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,38,39,52,61,62,63,69,73,74,75,77,83,85,86,89,91,92,93,94,95,97,101,102,104,],[-47,15,-5,-4,-8,15,15,-9,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-20,15,15,15,-24,-25,-15,15,15,15,-11,-16,-17,-18,15,15,-22,-12,-23,-26,-21,]),'STRING':([0,2,3,4,5,8,11,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,38,39,52,61,62,63,69,73,74,75,77,83,85,86,89,91,92,93,94,95,97,101,102,104,],[-47,16,-5,-4,-8,16,16,-9,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-20,16,16,16,-24,-25,-15,16,16,16,-11,-16,-17,-18,16,16,-22,-12,-23,-26,-21,]),'LPAREN':([0,2,3,4,5,7,8,9,11,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,38,39,52,61,62,63,69,73,74,75,77,80,83,85,86,89,91,92,93,94,95,97,101,102,104,],[-47,8,-5,-4,-8,31,8,34,38,-9,8,8,8,8,8,8,8,8,8,8,8,8,52,8,8,38,38,69,-20,8,8,69,-24,-25,-15,8,93,8,8,-11,-16,-17,-18,8,8,-22,-12,-23,-26,-21,]),'$end':([0,1,2,3,4,5,17,61,73,74,75,86,89,91,92,97,102,104,],[-47,0,-1,-5,-4,-8,-9,-20,-24,-25,-15,-11,-16,-17,-18,-12,-26,-21,]),'END_BLOCK':([5,17,61,73,74,75,86,89,91,92,94,95,97,101,102,104,],[-8,-9,-20,-24,-25,-15,-11,-16,-17,-18,100,-22,-12,-23,-26,-21,]),'ADD':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,57,58,66,68,72,81,82,90,96,],[18,-10,-2,-3,-6,-7,18,-10,18,-34,-35,-36,-37,-38,18,18,18,18,18,18,-45,18,18,-46,18,-10,18,18,18,18,18,]),'REM':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,57,58,66,68,72,81,82,90,96,],[19,-10,-2,-3,-6,-7,19,-10,19,-34,-35,-36,-37,-38,19,19,19,19,19,19,-45,19,19,-46,19,-10,19,19,19,19,19,]),'MUL':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,57,58,66,68,72,81,82,90,96,],[20,-10,-2,-3,-6,-7,20,-10,20,20,20,-36,-37,-38,20,20,20,20,20,20,-45,20,20,-46,20,-10,20,20,20,20,20,]),'DIV':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,57,58,66,68,72,81,82,90,96,],[21,-10,-2,-3,-6,-7,21,-10,21,21,21,-36,-37,-38,21,21,21,21,21,21,-45,21,21,-46,21,-10,21,21,21,21,21,]),'MOD':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,57,58,66,68,72,81,82,90,96,],[22,-10,-2,-3,-6,-7,22,-10,22,22,22,-36,-37,-38,22,22,22,22,22,22,-45,22,22,-46,22,-10,22,22,22,22,22,]),'GT':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,57,58,66,68,72,81,82,90,96,],[23,-10,-2,-3,-6,-7,23,-10,23,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,23,23,-46,23,-10,23,23,23,23,23,]),'LT':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,57,58,66,68,72,81,82,90,96,],[24,-10,-2,-3,-6,-7,24,-10,24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,24,24,-46,24,-10,24,24,24,24,24,]),'GE':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,57,58,66,68,72,81,82,90,96,],[25,-10,-2,-3,-6,-7,25,-10,25,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,25,25,-46,25,-10,25,25,25,25,25,]),'LE':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,57,58,66,68,72,81,82,90,96,],[26,-10,-2,-3,-6,-7,26,-10,26,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,26,26,-46,26,-10,26,26,26,26,26,]),'EQ':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,57,58,66,68,72,81,82,90,96,],[27,-10,-2,-3,-6,-7,27,-10,27,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,27,27,-46,27,-10,27,27,27,27,27,]),'NE':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,57,58,66,68,72,81,82,90,96,],[28,-10,-2,-3,-6,-7,28,-10,28,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,28,28,-46,28,-10,28,28,28,28,28,]),'POW':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,57,58,66,68,72,81,82,90,96,],[29,-10,-2,-3,-6,-7,29,-10,29,29,29,29,29,29,29,29,29,29,29,29,-45,29,29,-46,29,-10,29,29,29,29,29,]),'ASSIGN':([7,],[30,]),'RPAREN':([13,14,15,16,31,32,33,40,41,42,43,44,45,46,47,48,49,50,51,52,56,57,58,59,65,66,68,71,72,81,82,84,90,98,99,],[-2,-3,-6,-7,55,58,-10,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,70,76,-28,-46,78,84,58,-10,87,58,-31,-32,-33,-29,-14,103,]),'AND':([13,14,15,16,33,36,37,40,41,42,43,44,45,46,47,48,49,50,51,53,54,58,65,66,67,68,72,81,82,84,],[-2,-3,-6,-7,-10,62,-30,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,62,-46,62,-30,62,-10,-30,-31,-32,-33,]),'OR':([13,14,15,16,33,36,37,40,41,42,43,44,45,46,47,48,49,50,51,53,54,58,65,66,67,68,72,81,82,84,],[-2,-3,-6,-7,-10,63,-30,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-30,63,-46,63,-30,63,-10,-30,-31,-32,-33,]),'START_BLOCK':([13,14,15,16,33,36,37,40,41,42,43,44,45,46,47,48,49,50,51,58,70,79,81,82,84,87,103,],[-2,-3,-6,-7,-10,64,-30,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,64,64,-31,-32,-33,64,-19,]),'COMMA':([13,14,15,16,33,40,41,42,43,44,45,46,47,48,49,50,51,56,57,58,59,68,71,90,98,99,],[-2,-3,-6,-7,-10,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,77,-28,-46,77,-13,88,-29,-14,77,]),'ELSE':([13,14,15,16,33,37,40,41,42,43,44,45,46,47,48,49,50,51,58,67,81,82,84,],[-2,-3,-6,-7,-10,-30,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,85,-31,-32,-33,]),'IN':([35,],[60,]),'RANGE':([60,],[80,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'entry':([0,],[1,]),'start':([0,],[2,]),'empty':([0,],[3,]),'stmt':([2,83,94,],[4,95,101,]),'expression':([2,8,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,38,39,52,62,63,69,77,83,85,93,94,],[6,32,37,40,41,42,43,44,45,46,47,48,49,50,51,53,57,57,66,37,72,81,82,72,90,6,96,57,6,]),'if_assign':([2,83,94,],[12,12,12,]),'condition_list':([11,30,38,39,52,69,],[36,54,65,67,65,65,]),'expr_list':([31,34,93,],[56,59,99,]),'block_format':([36,70,79,87,],[61,86,92,97,]),'func_params':([52,],[71,]),'range':([60,],[79,]),'block':([83,],[94,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> entry","S'",1,None,None,None),
  ('entry -> start','entry',1,'p_entry','dyacc.py',14),
  ('expression -> TRUE','expression',1,'p_expression_true','expressionEndRule.py',14),
  ('expression -> FALSE','expression',1,'p_expression_false','expressionEndRule.py',19),
  ('start -> start stmt','start',2,'p_start','dyacc.py',21),
  ('start -> empty','start',1,'p_start','dyacc.py',22),
  ('expression -> NUMBER','expression',1,'p_expression_num','expressionEndRule.py',24),
  ('expression -> STRING','expression',1,'p_expression_string','expressionEndRule.py',29),
  ('stmt -> SPLIT','stmt',1,'p_stmt_none','dyacc.py',30),
  ('stmt -> expression SPLIT','stmt',2,'p_stmt_expr','dyacc.py',34),
  ('expression -> VAR','expression',1,'p_expression_var','expressionEndRule.py',34),
  ('stmt -> VAR ASSIGN LPAREN RPAREN block_format','stmt',5,'p_stmt_func_define_non_params','dyacc.py',40),
  ('stmt -> VAR ASSIGN LPAREN func_params RPAREN block_format','stmt',6,'p_stmt_func_define_params','dyacc.py',49),
  ('func_params -> VAR','func_params',1,'p_func_params_list','dyacc.py',58),
  ('func_params -> func_params COMMA VAR','func_params',3,'p_func_params_list','dyacc.py',59),
  ('stmt -> VAR LPAREN RPAREN SPLIT','stmt',4,'p_stmt_func_exe_non_params','dyacc.py',68),
  ('stmt -> VAR LPAREN expr_list RPAREN SPLIT','stmt',5,'p_stmt_func_exe_params','dyacc.py',74),
  ('stmt -> PRINT LPAREN expr_list RPAREN SPLIT','stmt',5,'p_stmt_print','dyacc.py',81),
  ('stmt -> FOR VAR IN range block_format','stmt',5,'p_stmt_for','dyacc.py',88),
  ('range -> RANGE LPAREN expr_list RPAREN','range',4,'p_range','dyacc.py',96),
  ('stmt -> IF condition_list block_format','stmt',3,'p_stmt_if_block','dyacc.py',103),
  ('block_format -> START_BLOCK SPLIT block END_BLOCK SPLIT','block_format',5,'p_block_format','dyacc.py',111),
  ('block -> stmt','block',1,'p_block','dyacc.py',116),
  ('block -> block stmt','block',2,'p_block','dyacc.py',117),
  ('stmt -> VAR ASSIGN expression SPLIT','stmt',4,'p_stmt_assign','dyacc.py',129),
  ('stmt -> VAR ASSIGN condition_list SPLIT','stmt',4,'p_stmt_assign','dyacc.py',130),
  ('stmt -> if_assign IF condition_list ELSE expression SPLIT','stmt',6,'p_stmt_triple_assign','dyacc.py',137),
  ('if_assign -> VAR ASSIGN expression','if_assign',3,'p_ifassign','dyacc.py',146),
  ('expr_list -> expression','expr_list',1,'p_expression_list','dyacc.py',157),
  ('expr_list -> expr_list COMMA expression','expr_list',3,'p_expression_list','dyacc.py',158),
  ('condition_list -> expression','condition_list',1,'p_condition_list','dyacc.py',169),
  ('condition_list -> condition_list AND expression','condition_list',3,'p_condition_list','dyacc.py',170),
  ('condition_list -> condition_list OR expression','condition_list',3,'p_condition_list','dyacc.py',171),
  ('condition_list -> LPAREN condition_list RPAREN','condition_list',3,'p_condition_parens','dyacc.py',182),
  ('expression -> expression ADD expression','expression',3,'p_expression_two_operator','dyacc.py',189),
  ('expression -> expression REM expression','expression',3,'p_expression_two_operator','dyacc.py',190),
  ('expression -> expression MUL expression','expression',3,'p_expression_two_operator','dyacc.py',191),
  ('expression -> expression DIV expression','expression',3,'p_expression_two_operator','dyacc.py',192),
  ('expression -> expression MOD expression','expression',3,'p_expression_two_operator','dyacc.py',193),
  ('expression -> expression GT expression','expression',3,'p_expression_two_operator','dyacc.py',194),
  ('expression -> expression LT expression','expression',3,'p_expression_two_operator','dyacc.py',195),
  ('expression -> expression GE expression','expression',3,'p_expression_two_operator','dyacc.py',196),
  ('expression -> expression LE expression','expression',3,'p_expression_two_operator','dyacc.py',197),
  ('expression -> expression EQ expression','expression',3,'p_expression_two_operator','dyacc.py',198),
  ('expression -> expression NE expression','expression',3,'p_expression_two_operator','dyacc.py',199),
  ('expression -> expression POW expression','expression',3,'p_expression_two_operator','dyacc.py',200),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_parens','dyacc.py',207),
  ('empty -> <empty>','empty',0,'p_empty','dyacc.py',223),
]
