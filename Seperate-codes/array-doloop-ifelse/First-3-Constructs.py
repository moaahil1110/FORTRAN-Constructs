import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = [
    'DO', 'IF', 'ELSE', 'ENDIF', 'ENDDO', 'THEN', 'IDENTIFIER', 'NUMBER',
    'INTEGER', 'REAL', 'CHARACTER', 'LOGICAL', 'DCOLON', 'EQUALS', 'COMMA', 
    'LPAREN', 'RPAREN', 'GT', 'LT', 'GE', 'LE', 'EQ', 'NE', 'PLUS', 'MINUS',
    'TIMES', 'DIVIDE', 'POWER', 'STRING', 'TRUE', 'FALSE', 'AND', 'OR', 'NOT',
    'CONTINUE', 'EXIT', 'PRINT', 'READ', 'DIMENSION'
]

t_DCOLON = r'::'
t_EQUALS = r'='
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\*\*'

def t_GT(t):
    r'\.GT\.'
    return t

def t_LT(t):
    r'\.LT\.'
    return t

def t_GE(t):
    r'\.GE\.'
    return t

def t_LE(t):
    r'\.LE\.'
    return t

def t_EQ(t):
    r'\.EQ\.'
    return t

def t_NE(t):
    r'\.NE\.'
    return t

def t_AND(t):
    r'\.AND\.'
    return t

def t_OR(t):
    r'\.OR\.'
    return t

def t_NOT(t):
    r'\.NOT\.'
    return t

def t_TRUE(t):
    r'\.TRUE\.'
    return t

def t_FALSE(t):
    r'\.FALSE\.'
    return t

# Keywords
def t_DO(t):
    r'DO'
    return t

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

def t_ENDDO(t):
    r'ENDDO'
    return t

def t_INTEGER(t):
    r'INTEGER'
    return t

def t_REAL(t):
    r'REAL'
    return t

def t_CHARACTER(t):
    r'CHARACTER'
    return t

def t_LOGICAL(t):
    r'LOGICAL'
    return t

def t_CONTINUE(t):
    r'CONTINUE'
    return t

def t_EXIT(t):
    r'EXIT'
    return t

def t_PRINT(t):
    r'PRINT'
    return t

def t_READ(t):
    r'READ'
    return t

def t_DIMENSION(t):
    r'DIMENSION'
    return t

def t_NUMBER(t):
    r'\d*\.?\d+([eE][-+]?\d+)?'
    try:
        t.value = float(t.value)
    except ValueError:
        print(f"Float value too large: {t.value}")
        t.value = 0
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    return t

def t_STRING(t):
    r'\'[^\']*\'|\"[^\"]*\"'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_COMMENT(t):
    r'![^\n]*'
    pass

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
"""
INTEGER :: array(100)
DO i = 1, 100
    IF (x .GT. 0) THEN
        array(i) = i * 2
    ENDIF
ENDDO
"""
# Grammar Rules
def p_program(p):
    '''program : statement
               | program statement'''
    pass

def p_statement(p):
    '''statement : declaration
                | assignment
                | if_statement
                | do_loop
                | io_statement
                | CONTINUE
                | EXIT'''
    pass

def p_declaration(p):
    '''declaration : type DCOLON IDENTIFIER
                  | type DCOLON IDENTIFIER LPAREN array_dims RPAREN
                  | DIMENSION DCOLON IDENTIFIER LPAREN array_dims RPAREN'''
    pass

def p_type(p):
    '''type : INTEGER
            | REAL
            | CHARACTER
            | LOGICAL'''
    pass

def p_array_dims(p):
    '''array_dims : NUMBER
                 | IDENTIFIER
                 | array_dims COMMA NUMBER
                 | array_dims COMMA IDENTIFIER'''
    pass

def p_assignment(p):
    '''assignment : target EQUALS expression'''
    pass

def p_target(p):
    '''target : IDENTIFIER
              | array_ref'''
    pass

def p_array_ref(p):
    '''array_ref : IDENTIFIER LPAREN expression RPAREN
                | IDENTIFIER LPAREN expression_list RPAREN'''
    pass

def p_if_statement(p):
    '''if_statement : IF LPAREN condition RPAREN THEN statement_list ENDIF
                   | IF LPAREN condition RPAREN THEN statement_list ELSE statement_list ENDIF'''
    pass

def p_do_loop(p):
    '''do_loop : DO IDENTIFIER EQUALS expression COMMA expression statement_list ENDDO'''
    pass

def p_statement_list(p):
    '''statement_list : statement
                     | statement_list statement'''
    pass

def p_io_statement(p):
    '''io_statement : PRINT TIMES COMMA print_list
                   | READ TIMES COMMA read_list'''
    pass

def p_print_list(p):
    '''print_list : expression
                 | STRING
                 | print_list COMMA expression
                 | print_list COMMA STRING'''
    pass

def p_read_list(p):
    '''read_list : IDENTIFIER
                | read_list COMMA IDENTIFIER'''
    pass

# Modified expression rules
def p_expression(p):
    '''expression : term
                 | expression PLUS term
                 | expression MINUS term'''
    pass

def p_term(p):
    '''term : factor
            | term TIMES factor
            | term DIVIDE factor'''
    pass

def p_factor(p):
    '''factor : primary
              | factor POWER primary'''
    pass

def p_primary(p):
    '''primary : NUMBER
               | IDENTIFIER
               | LPAREN expression RPAREN
               | array_ref'''  # Added array_ref here
    pass

def p_expression_list(p):
    '''expression_list : expression
                      | expression_list COMMA expression'''
    pass

def p_condition(p):
    '''condition : expression GT expression
                | expression LT expression
                | expression GE expression
                | expression LE expression
                | expression EQ expression
                | expression NE expression
                | condition AND condition
                | condition OR condition
                | NOT condition
                | LPAREN condition RPAREN
                | TRUE
                | FALSE'''
    pass

def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, token={p.type}, value={p.value}")
    else:
        print("Syntax error at EOF")
lexer = lex.lex()
parser = yacc.yacc()

def interactive_parser():
    """
    Interactive FORTRAN code parser that accepts multi-line input from users.
    """
    print("\n=== FORTRAN Syntax Validator ===")
    print("Instructions:")
    print("1. Enter your FORTRAN code line by line")
    print("2. Press Enter twice (i.e., input a blank line) to finish your input")
    print("3. Type 'EXIT' to quit the program")
    print("4. Type 'HELP' to see example inputs")
    print("=" * 40)

    def show_help():
        print("\nExample FORTRAN Constructs:")
        print("\n1. Array Declaration:")
        print("INTEGER :: array(100)")
        print("REAL :: matrix(10, 10)")
        
        print("\n2. DO Loop:")
        print("DO i = 1, 10")
        print("    x(i) = i * 2")
        print("ENDDO")
        
        print("\n3. IF Statement:")
        print("IF (x .GT. 0) THEN")
        print("    y = x * 2")
        print("ELSE")
        print("    y = 0")
        print("ENDIF")
        
        print("\n4. Input/Output:")
        print("READ *, x")
        print("PRINT *, 'Value:', x")
        print("\nEnter your code following these patterns.")
        print("=" * 40)

    def parse_input(code):
        try:
            lexer.lineno = 1
            parser.parse(code, lexer=lexer)
            return True
        except Exception as e:
            print(f"\nError parsing code: {str(e)}")
            return False

    while True:
        print("\nEnter your FORTRAN code (Enter twice to parse, 'EXIT' to quit, 'HELP' for examples):")
        code_lines = []
        
        while True:
            try:
                line = input()
                
                if not code_lines and line.upper() == 'EXIT':
                    print("Exiting the parser. Goodbye!")
                    return
                elif not code_lines and line.upper() == 'HELP':
                    show_help()
                    break
                elif line.strip() == '':
                    if code_lines:
                        break
                    continue
                
                code_lines.append(line)
                
            except EOFError:
                print("\nInput terminated. Exiting.")
                return
            except KeyboardInterrupt:
                print("\nOperation cancelled by user. Please try again.")
                code_lines = []
                break

        if code_lines:
            code = '\n'.join(code_lines)
            print("\nParsing the following code:")
            print("-" * 40)
            print(code)
            print("-" * 40)
            
            success = parse_input(code)
            
            if success:
                print("\nSyntax is valid! ✓")
            else:
                print("\nSyntax contains errors. Please check your code and try again.")
            
            print("\nReady for next input...")

if __name__ == "__main__":
    try:
        interactive_parser()
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)