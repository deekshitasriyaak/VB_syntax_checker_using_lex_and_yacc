import ply.yacc as yacc
from for_lex import tokens
validsyntax=True

def p_statement(p):
    '''statement : FOR STATEMENTS EQUALS NUMBER TO NUMBER optional_step stats optional_exit stats NEXT STATEMENTS stats
                 | FOR STATEMENTS EQUALS NUMBER TO NUMBER optional_step optional_exit NEXT STATEMENTS
                 | FOR STATEMENTS EQUALS NUMBER TO NUMBER optional_step stats optional_exit NEXT STATEMENTS
                 | FOR STATEMENTS EQUALS NUMBER TO NUMBER optional_step optional_exit NEXT STATEMENTS stats
                 | FOR STATEMENTS EQUALS NUMBER TO NUMBER optional_step optional_exit stats NEXT STATEMENTS
                 '''
    global validsyntax
    validsyntax = True
def p_stats(p):
    '''stats : STATEMENTS
                | stats stats
                | statement'''

def p_optional_step(p):
    '''
    optional_step : STEP NUMBER
                  | empty
    '''
    if len(p) == 3:
        p[0] = p[2]
def p_optional_exit(p):
    '''
    optional_exit : EXIT FOR
                  | empty
    '''
    pass
def p_empty(p):
    'empty :'
    pass

def p_error(p):
    global validsyntax
    validsyntax = False
    print(f"Syntax error at {p.value}")

# Build the parser
parser = yacc.yacc()

# Read the input from a file or string
input_str="""
For j = 1 To 10 Step 2
Next j=j+1"""

# Parse the input
parser.parse(input_str)

if validsyntax:
    print("Valid Syntax")
else:
    print("Invalid Syntax")
