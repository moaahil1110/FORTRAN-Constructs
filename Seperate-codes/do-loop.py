import ply.lex as lex
import ply.yacc as yacc

# Token list for DO loop
tokens = [
    'DO', 'ENDDO', 'IDENTIFIER', 'NUMBER', 'EQUALS', 'COMMA',
    'LPAREN', 'RPAREN', 'PLUS'
]

# Token definitions
def t_DO(t):
    r'DO'
    return t

def t_ENDDO(t):
    r'ENDDO'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_EQUALS = r'='
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS = r'\+'

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
    '''program : do_loop'''
    print("DO loop parsed successfully")

def p_do_loop(p):
    '''do_loop : DO IDENTIFIER EQUALS NUMBER COMMA NUMBER statements ENDDO'''
    pass

def p_statements(p):
    '''statements : statement
                 | statements statement
                 | empty'''
    pass

def p_statement(p):
    '''statement : assignment'''
    pass

def p_assignment(p):
    '''assignment : IDENTIFIER LPAREN IDENTIFIER RPAREN EQUALS expression'''
    pass

def p_expression(p):
    '''expression : IDENTIFIER LPAREN IDENTIFIER RPAREN
                 | NUMBER
                 | IDENTIFIER LPAREN IDENTIFIER RPAREN PLUS NUMBER'''
    pass

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' at line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build parser
parser = yacc.yacc()

print("Fortran DO Loop Syntax Checker")
print("Enter DO loop (e.g., 'DO i = 1, 10')")
print("Type 'END' on a new line to finish input.")

user_input = ""
while True:
    line = input()
    if line.strip().upper() == 'END':
        break
    user_input += line + "\n"

result = parser.parse(user_input, tracking=True)