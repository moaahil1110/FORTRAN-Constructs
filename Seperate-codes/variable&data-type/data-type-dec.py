import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'IDENTIFIER',  
    'INTEGER',     
    'REAL',        
    'CHARACTER',   
    'COMMA',       
    'COLON',       
]
# Input Line: INTEGER :: x, y, z
t_COMMA = r','
t_COLON = r'::'

def t_INTEGER(t):
    r'INTEGER'
    return t

def t_REAL(t):
    r'REAL'
    return t

def t_CHARACTER(t):
    r'CHARACTER'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_declaration(p):
    '''declaration : type COLON variable_list'''
    p[0] = True
    print("Valid data-type declaration:", p[1], "::", p[3])

def p_type(p):
    '''type : INTEGER
            | REAL
            | CHARACTER'''
    p[0] = p[1]

def p_variable_list(p):
    '''variable_list : IDENTIFIER
                     | IDENTIFIER COMMA variable_list'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + ', ' + p[3]

def p_error(p):
    print("Syntax error in data-type declaration!")

parser = yacc.yacc()

data = input("Enter a data-type declaration (e.g., 'INTEGER :: x, y'): ")

result = parser.parse(data)

if result:
    print("Parsing successful!")
else:
    print("Parsing failed!")
