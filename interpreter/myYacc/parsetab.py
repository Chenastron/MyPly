
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftLTLEGTGEEQNEleftREMADDleftMULDIVMODleftPOWADD AND ASSIGN COLON COMMA DIV ELSE END_BLOCK EQ FALSE FOR GE GT IF IN LE LPAREN LT MOD MUL NE NUMBER OR POW PRINT RANGE REM RPAREN SPLIT START_BLOCK STRING TRUE VARentry : startexpression : TRUEexpression : FALSE\n    start : start stmt\n          | empty\n    expression : NUMBERexpression : STRINGstmt : SPLITstmt : expression SPLITexpression : VAR\n    stmt : VAR ASSIGN LPAREN RPAREN block_format\n    \n    stmt : VAR LPAREN RPAREN SPLIT\n    \n    stmt : PRINT LPAREN expr_list RPAREN SPLIT\n    stmt : FOR VAR IN range block_formatrange : RANGE LPAREN expr_list RPAREN\n    stmt : IF condition_list block_format\n    \n    block_format : START_BLOCK SPLIT block END_BLOCK SPLIT\n    \n    block : stmt\n          | block stmt\n    \n    stmt : VAR ASSIGN expression SPLIT\n         | VAR ASSIGN condition_list SPLIT\n    stmt : if_assign IF condition_list ELSE expression SPLITif_assign : VAR ASSIGN expression\n    expr_list : expression\n              | expr_list COMMA expression\n    \n    condition_list : expression\n                   | condition_list AND expression\n                   | condition_list OR expression\n    condition_list : LPAREN condition_list RPAREN\n    expression : expression ADD expression\n               | expression REM expression\n               | expression MUL expression\n               | expression DIV expression\n               | expression MOD expression\n               | expression GT expression\n               | expression LT expression\n               | expression GE expression\n               | expression LE expression\n               | expression EQ expression\n               | expression NE expression\n               | expression POW expression\n    expression : LPAREN expression RPARENempty :'
    
_lr_action_items = {'SPLIT':([0,2,3,4,5,6,7,13,14,15,16,17,33,40,41,42,43,44,45,46,47,48,49,50,51,53,54,55,56,60,63,70,71,72,73,77,78,79,80,82,83,85,87,88,89,91,92,93,95,],[-43,5,-5,-4,-8,17,-10,-2,-3,-6,-7,-9,-10,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,70,71,72,-42,-16,79,-20,-21,-12,83,-27,-28,5,-29,-11,-13,-14,5,-18,93,95,-19,-22,-17,]),'VAR':([0,2,3,4,5,8,10,11,17,18,19,20,21,22,23,24,25,26,27,28,29,30,34,38,39,52,60,61,62,67,70,71,72,74,79,81,82,83,85,86,87,88,92,93,95,],[-43,7,-5,-4,-8,33,35,33,-9,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-16,33,33,33,-20,-21,-12,33,7,33,-11,-13,-14,33,7,-18,-19,-22,-17,]),'PRINT':([0,2,3,4,5,17,60,70,71,72,79,82,83,85,87,88,92,93,95,],[-43,9,-5,-4,-8,-9,-16,-20,-21,-12,9,-11,-13,-14,9,-18,-19,-22,-17,]),'FOR':([0,2,3,4,5,17,60,70,71,72,79,82,83,85,87,88,92,93,95,],[-43,10,-5,-4,-8,-9,-16,-20,-21,-12,10,-11,-13,-14,10,-18,-19,-22,-17,]),'IF':([0,2,3,4,5,12,13,14,15,16,17,33,40,41,42,43,44,45,46,47,48,49,50,51,53,56,60,70,71,72,79,82,83,85,87,88,92,93,95,],[-43,11,-5,-4,-8,39,-2,-3,-6,-7,-9,-10,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-23,-42,-16,-20,-21,-12,11,-11,-13,-14,11,-18,-19,-22,-17,]),'TRUE':([0,2,3,4,5,8,11,17,18,19,20,21,22,23,24,25,26,27,28,29,30,34,38,39,52,60,61,62,67,70,71,72,74,79,81,82,83,85,86,87,88,92,93,95,],[-43,13,-5,-4,-8,13,13,-9,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,-16,13,13,13,-20,-21,-12,13,13,13,-11,-13,-14,13,13,-18,-19,-22,-17,]),'FALSE':([0,2,3,4,5,8,11,17,18,19,20,21,22,23,24,25,26,27,28,29,30,34,38,39,52,60,61,62,67,70,71,72,74,79,81,82,83,85,86,87,88,92,93,95,],[-43,14,-5,-4,-8,14,14,-9,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-16,14,14,14,-20,-21,-12,14,14,14,-11,-13,-14,14,14,-18,-19,-22,-17,]),'NUMBER':([0,2,3,4,5,8,11,17,18,19,20,21,22,23,24,25,26,27,28,29,30,34,38,39,52,60,61,62,67,70,71,72,74,79,81,82,83,85,86,87,88,92,93,95,],[-43,15,-5,-4,-8,15,15,-9,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-16,15,15,15,-20,-21,-12,15,15,15,-11,-13,-14,15,15,-18,-19,-22,-17,]),'STRING':([0,2,3,4,5,8,11,17,18,19,20,21,22,23,24,25,26,27,28,29,30,34,38,39,52,60,61,62,67,70,71,72,74,79,81,82,83,85,86,87,88,92,93,95,],[-43,16,-5,-4,-8,16,16,-9,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-16,16,16,16,-20,-21,-12,16,16,16,-11,-13,-14,16,16,-18,-19,-22,-17,]),'LPAREN':([0,2,3,4,5,7,8,9,11,17,18,19,20,21,22,23,24,25,26,27,28,29,30,34,38,39,52,60,61,62,67,70,71,72,74,76,79,81,82,83,85,86,87,88,92,93,95,],[-43,8,-5,-4,-8,31,8,34,38,-9,8,8,8,8,8,8,8,8,8,8,8,8,52,8,38,38,67,-16,8,8,67,-20,-21,-12,8,86,8,8,-11,-13,-14,8,8,-18,-19,-22,-17,]),'$end':([0,1,2,3,4,5,17,60,70,71,72,82,83,85,93,95,],[-43,0,-1,-5,-4,-8,-9,-16,-20,-21,-12,-11,-13,-14,-22,-17,]),'END_BLOCK':([5,17,60,70,71,72,82,83,85,87,88,92,93,95,],[-8,-9,-16,-20,-21,-12,-11,-13,-14,91,-18,-19,-22,-17,]),'ADD':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,56,58,65,69,77,78,84,89,],[18,-10,-2,-3,-6,-7,18,-10,18,-30,-31,-32,-33,-34,18,18,18,18,18,18,-41,18,-42,18,18,18,18,18,18,18,]),'REM':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,56,58,65,69,77,78,84,89,],[19,-10,-2,-3,-6,-7,19,-10,19,-30,-31,-32,-33,-34,19,19,19,19,19,19,-41,19,-42,19,19,19,19,19,19,19,]),'MUL':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,56,58,65,69,77,78,84,89,],[20,-10,-2,-3,-6,-7,20,-10,20,20,20,-32,-33,-34,20,20,20,20,20,20,-41,20,-42,20,20,20,20,20,20,20,]),'DIV':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,56,58,65,69,77,78,84,89,],[21,-10,-2,-3,-6,-7,21,-10,21,21,21,-32,-33,-34,21,21,21,21,21,21,-41,21,-42,21,21,21,21,21,21,21,]),'MOD':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,56,58,65,69,77,78,84,89,],[22,-10,-2,-3,-6,-7,22,-10,22,22,22,-32,-33,-34,22,22,22,22,22,22,-41,22,-42,22,22,22,22,22,22,22,]),'GT':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,56,58,65,69,77,78,84,89,],[23,-10,-2,-3,-6,-7,23,-10,23,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,23,-42,23,23,23,23,23,23,23,]),'LT':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,56,58,65,69,77,78,84,89,],[24,-10,-2,-3,-6,-7,24,-10,24,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,24,-42,24,24,24,24,24,24,24,]),'GE':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,56,58,65,69,77,78,84,89,],[25,-10,-2,-3,-6,-7,25,-10,25,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,25,-42,25,25,25,25,25,25,25,]),'LE':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,56,58,65,69,77,78,84,89,],[26,-10,-2,-3,-6,-7,26,-10,26,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,26,-42,26,26,26,26,26,26,26,]),'EQ':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,56,58,65,69,77,78,84,89,],[27,-10,-2,-3,-6,-7,27,-10,27,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,27,-42,27,27,27,27,27,27,27,]),'NE':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,56,58,65,69,77,78,84,89,],[28,-10,-2,-3,-6,-7,28,-10,28,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,28,-42,28,28,28,28,28,28,28,]),'POW':([6,7,13,14,15,16,32,33,37,40,41,42,43,44,45,46,47,48,49,50,51,53,56,58,65,69,77,78,84,89,],[29,-10,-2,-3,-6,-7,29,-10,29,29,29,29,29,29,29,29,29,29,29,29,-41,29,-42,29,29,29,29,29,29,29,]),'ASSIGN':([7,],[30,]),'RPAREN':([13,14,15,16,31,32,33,40,41,42,43,44,45,46,47,48,49,50,51,52,56,57,58,64,65,69,77,78,80,84,90,],[-2,-3,-6,-7,55,56,-10,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,68,-42,73,-24,80,56,56,-27,-28,-29,-25,94,]),'AND':([13,14,15,16,33,36,37,40,41,42,43,44,45,46,47,48,49,50,51,53,54,56,64,65,66,69,77,78,80,],[-2,-3,-6,-7,-10,61,-26,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,61,-42,61,-26,61,-26,-27,-28,-29,]),'OR':([13,14,15,16,33,36,37,40,41,42,43,44,45,46,47,48,49,50,51,53,54,56,64,65,66,69,77,78,80,],[-2,-3,-6,-7,-10,62,-26,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-26,62,-42,62,-26,62,-26,-27,-28,-29,]),'START_BLOCK':([13,14,15,16,33,36,37,40,41,42,43,44,45,46,47,48,49,50,51,56,68,75,77,78,80,94,],[-2,-3,-6,-7,-10,63,-26,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,63,63,-27,-28,-29,-15,]),'COMMA':([13,14,15,16,33,40,41,42,43,44,45,46,47,48,49,50,51,56,57,58,84,90,],[-2,-3,-6,-7,-10,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,74,-24,-25,74,]),'ELSE':([13,14,15,16,33,37,40,41,42,43,44,45,46,47,48,49,50,51,56,66,77,78,80,],[-2,-3,-6,-7,-10,-26,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,81,-27,-28,-29,]),'IN':([35,],[59,]),'RANGE':([59,],[76,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'entry':([0,],[1,]),'start':([0,],[2,]),'empty':([0,],[3,]),'stmt':([2,79,87,],[4,88,92,]),'expression':([2,8,11,18,19,20,21,22,23,24,25,26,27,28,29,30,34,38,39,52,61,62,67,74,79,81,86,87,],[6,32,37,40,41,42,43,44,45,46,47,48,49,50,51,53,58,65,37,69,77,78,69,84,6,89,58,6,]),'if_assign':([2,79,87,],[12,12,12,]),'condition_list':([11,30,38,39,52,67,],[36,54,64,66,64,64,]),'expr_list':([34,86,],[57,90,]),'block_format':([36,68,75,],[60,82,85,]),'range':([59,],[75,]),'block':([79,],[87,]),}

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
  ('stmt -> VAR ASSIGN LPAREN RPAREN block_format','stmt',5,'p_stmt_func_define','dyacc.py',40),
  ('stmt -> VAR LPAREN RPAREN SPLIT','stmt',4,'p_stmt_func_exe','dyacc.py',48),
  ('stmt -> PRINT LPAREN expr_list RPAREN SPLIT','stmt',5,'p_stmt_print','dyacc.py',56),
  ('stmt -> FOR VAR IN range block_format','stmt',5,'p_stmt_for','dyacc.py',63),
  ('range -> RANGE LPAREN expr_list RPAREN','range',4,'p_range','dyacc.py',71),
  ('stmt -> IF condition_list block_format','stmt',3,'p_stmt_if_block','dyacc.py',78),
  ('block_format -> START_BLOCK SPLIT block END_BLOCK SPLIT','block_format',5,'p_block_format','dyacc.py',86),
  ('block -> stmt','block',1,'p_block','dyacc.py',91),
  ('block -> block stmt','block',2,'p_block','dyacc.py',92),
  ('stmt -> VAR ASSIGN expression SPLIT','stmt',4,'p_stmt_assign','dyacc.py',104),
  ('stmt -> VAR ASSIGN condition_list SPLIT','stmt',4,'p_stmt_assign','dyacc.py',105),
  ('stmt -> if_assign IF condition_list ELSE expression SPLIT','stmt',6,'p_stmt_triple_assign','dyacc.py',112),
  ('if_assign -> VAR ASSIGN expression','if_assign',3,'p_ifassign','dyacc.py',121),
  ('expr_list -> expression','expr_list',1,'p_expression_list','dyacc.py',132),
  ('expr_list -> expr_list COMMA expression','expr_list',3,'p_expression_list','dyacc.py',133),
  ('condition_list -> expression','condition_list',1,'p_condition_list','dyacc.py',144),
  ('condition_list -> condition_list AND expression','condition_list',3,'p_condition_list','dyacc.py',145),
  ('condition_list -> condition_list OR expression','condition_list',3,'p_condition_list','dyacc.py',146),
  ('condition_list -> LPAREN condition_list RPAREN','condition_list',3,'p_condition_parens','dyacc.py',157),
  ('expression -> expression ADD expression','expression',3,'p_expression_two_operator','dyacc.py',164),
  ('expression -> expression REM expression','expression',3,'p_expression_two_operator','dyacc.py',165),
  ('expression -> expression MUL expression','expression',3,'p_expression_two_operator','dyacc.py',166),
  ('expression -> expression DIV expression','expression',3,'p_expression_two_operator','dyacc.py',167),
  ('expression -> expression MOD expression','expression',3,'p_expression_two_operator','dyacc.py',168),
  ('expression -> expression GT expression','expression',3,'p_expression_two_operator','dyacc.py',169),
  ('expression -> expression LT expression','expression',3,'p_expression_two_operator','dyacc.py',170),
  ('expression -> expression GE expression','expression',3,'p_expression_two_operator','dyacc.py',171),
  ('expression -> expression LE expression','expression',3,'p_expression_two_operator','dyacc.py',172),
  ('expression -> expression EQ expression','expression',3,'p_expression_two_operator','dyacc.py',173),
  ('expression -> expression NE expression','expression',3,'p_expression_two_operator','dyacc.py',174),
  ('expression -> expression POW expression','expression',3,'p_expression_two_operator','dyacc.py',175),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_parens','dyacc.py',182),
  ('empty -> <empty>','empty',0,'p_empty','dyacc.py',198),
]
