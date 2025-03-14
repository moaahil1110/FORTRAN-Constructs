import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'IDENTIFIER', 
    'COMMA',       
]

t_COMMA = r','
# Input Line: x, y, z
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_variable_list(p):
    '''variable_list : IDENTIFIER
                     | IDENTIFIER COMMA variable_list'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + ', ' + p[3]
    print("Valid variable declaration:", p[0])

def p_error(p):
    print("Syntax error in variable declaration!")

parser = yacc.yacc()

data = input("Enter a variable declaration (e.g., 'x, y, z'): ")

result = parser.parse(data)

if result:
    print("Parsing successful!")
else:
    print("Parsing failed!")
