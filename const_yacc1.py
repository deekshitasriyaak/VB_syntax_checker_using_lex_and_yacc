import ply.yacc as yacc
from const_lex import tokens

syntax_valid = True

def p_program(p):
    '''
    program : empty
            | program declaration
    '''
    pass

def p_declaration(p):
    '''
    declaration : access_modifier CONST parttwo
                | CONST parttwo
    '''
    #print(f"Variable declaration: {p[1]} {p[2]} {', '.join(p[3])} {p[4]} {p[5]} {p[6]} {p[7]}")

def p_parttwo(p):
    '''parttwo : var_list AS DTYPE EQUALS expression
                | parttwo COMMA parttwo'''

def p_var_list(p):
    '''
    var_list : var_list COMMA VAR
             | VAR
    '''
    if len(p) > 2:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_access_modifier(p):
    '''
    access_modifier : PUBLIC
                    | PRIVATE
                    | empty
    '''
    p[0] = p[1] if len(p) > 1 else ''

def p_expression(p):
    '''
    expression : NUM
               | STRING
    '''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    global syntax_valid
    syntax_valid = False
    if p:
        print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Test input
input_code = """
Const conAge As Integer = 34, conWage As Currency = 2000
"""
parser.parse(input_code)

if syntax_valid:
    print("Syntax is valid")
else:
    print("Syntax is invalid")