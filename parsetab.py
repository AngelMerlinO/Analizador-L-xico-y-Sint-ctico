

_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN COMMA CONSOLE DIVIDE DOT EQ FOR GE GLOBAL GT ID LBRACE LE LOG LPAREN LT MINUS NE NUMBER PLUS RBRACE RPAREN SEMICOLON SINGLE_QUOTE STRING TIMES VARprogram : for_loop console_statementfor_loop : FOR LPAREN VAR ID ASSIGN NUMBER SEMICOLON ID LT NUMBER SEMICOLON ID PLUS PLUS RPAREN LBRACE block RBRACEconsole_statement : CONSOLE DOT LOG LPAREN expression RPAREN SEMICOLONexpression : SINGLE_QUOTE ID ID SINGLE_QUOTE PLUS ID\n                  | GLOBALblock : console_statement'
    
_lr_action_items = {'FOR':([0,],[3,]),'$end':([1,4,20,],[0,-1,-3,]),'CONSOLE':([2,33,36,],[5,5,-2,]),'LPAREN':([3,9,],[6,11,]),'DOT':([5,],[7,]),'VAR':([6,],[8,]),'LOG':([7,],[9,]),'ID':([8,14,18,19,25,28,],[10,18,21,22,27,29,]),'ASSIGN':([10,],[12,]),'SINGLE_QUOTE':([11,21,],[14,23,]),'GLOBAL':([11,],[15,]),'NUMBER':([12,24,],[16,26,]),'RPAREN':([13,15,27,31,],[17,-5,-4,32,]),'SEMICOLON':([16,17,26,],[19,20,28,]),'RBRACE':([20,34,35,],[-3,36,-6,]),'LT':([22,],[24,]),'PLUS':([23,29,30,],[25,30,31,]),'LBRACE':([32,],[33,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'for_loop':([0,],[2,]),'console_statement':([2,33,],[4,35,]),'expression':([11,],[13,]),'block':([33,],[34,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> for_loop console_statement','program',2,'p_program','parser_1.py',6),
  ('for_loop -> FOR LPAREN VAR ID ASSIGN NUMBER SEMICOLON ID LT NUMBER SEMICOLON ID PLUS PLUS RPAREN LBRACE block RBRACE','for_loop',18,'p_for_loop','parser_1.py',10),
  ('console_statement -> CONSOLE DOT LOG LPAREN expression RPAREN SEMICOLON','console_statement',7,'p_console_statement','parser_1.py',14),
  ('expression -> SINGLE_QUOTE ID ID SINGLE_QUOTE PLUS ID','expression',6,'p_expression','parser_1.py',18),
  ('expression -> GLOBAL','expression',1,'p_expression','parser_1.py',19),
  ('block -> console_statement','block',1,'p_block','parser_1.py',26),
]
