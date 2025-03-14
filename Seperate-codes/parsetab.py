
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA IDENTIFIERvariable_list : IDENTIFIER\n                     | IDENTIFIER COMMA variable_list'
    
_lr_action_items = {'IDENTIFIER':([0,3,],[2,2,]),'$end':([1,2,4,],[0,-1,-2,]),'COMMA':([2,],[3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'variable_list':([0,3,],[1,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> variable_list","S'",1,None,None,None),
  ('variable_list -> IDENTIFIER','variable_list',1,'p_variable_list','variable-dec.py',24),
  ('variable_list -> IDENTIFIER COMMA variable_list','variable_list',3,'p_variable_list','variable-dec.py',25),
]
