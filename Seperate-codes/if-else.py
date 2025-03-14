import ply.lex as lex
import ply.yacc as yacc

# Token list for IF-ELSE
tokens = [
    'IF', 'THEN', 'ELSE', 'ENDIF', 'IDENTIFIER', 'NUMBER',
    'LPAREN', 'RPAREN', 'GT', 'LT', 'EQUALS', 'PLUS'
]

# Token definitions
def t_IF(t):
    r'IF'
    return t

def t_THEN(t):
    r'THEN'
    return t

def t_ELSE(t):
    r'ELSE'
    return t

def t_ENDIF(t):
    r'ENDIF'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_GT = r'\.GT\.'
t_LT = r'\.LT\.'
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
    '''program : if_statement'''
    print("IF statement parsed successfully")

def p_if_statement(p):
    '''if_statement : IF LPAREN condition RPAREN THEN statements ELSE statements ENDIF
                   | IF LPAREN condition RPAREN THEN statements ENDIF'''
    pass

def p_condition(p):
    '''condition : array_ref GT NUMBER
                | array_ref LT NUMBER'''
    pass

def p_array_ref(p):
    '''array_ref : IDENTIFIER LPAREN IDENTIFIER RPAREN'''
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
    '''assignment : array_ref EQUALS expression'''
    pass

def p_expression(p):
    '''expression : array_ref
                 | NUMBER
                 | array_ref PLUS NUMBER'''
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

print("Fortran IF-ELSE Syntax Checker")
print("Enter IF-ELSE statement (e.g., 'IF (x .GT. 0) THEN')")
print("Type 'END' on a new line to finish input.")

user_input = ""
while True:
    line = input()
    if line.strip().upper() == 'END':
        break
    user_input += line + "\n"

result = parser.parse(user_input, tracking=True)