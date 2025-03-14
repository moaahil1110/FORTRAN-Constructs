import ply.lex as lex
import ply.yacc as yacc

# Token list for array declaration
tokens = [
    'INTEGER', 'DCOLON', 'IDENTIFIER', 'LPAREN', 'RPAREN', 'NUMBER'
]

# Token definitions
def t_INTEGER(t):
    r'INTEGER'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_DCOLON(t):
    r'::'
    return t

t_LPAREN = r'\('
t_RPAREN = r'\)'

# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Build lexer
lexer = lex.lex()

# Parsing rules
def p_program(p):
    '''program : declaration'''
    print("Array declaration parsed successfully")

def p_declaration(p):
    '''declaration : INTEGER DCOLON IDENTIFIER LPAREN NUMBER RPAREN'''
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' at line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build parser
parser = yacc.yacc()

print("Fortran Array Declaration Syntax Checker")
print("Enter array declaration (e.g., 'INTEGER :: array(10)')")
print("Type 'END' on a new line to finish input.")

user_input = ""
while True:
    line = input()
    if line.strip().upper() == 'END':
        break
    user_input += line + "\n"

result = parser.parse(user_input, tracking=True)