import ply.yacc as yacc
from with_lex import input_text
tokens = ('WITH', 'STATEMENTS', 'END', 'NEWLINE', 'TERM')
validsyntax=True

def p_statement(p):
    '''statement : prog'''
    global validsyntax
    validsyntax = True

def p_prog(p):
    '''prog : WITH TERM NEWLINE statements END WITH'''
    pass

def p_statements(p):
    '''statements : STATEMENTS
                | NEWLINE
                | statements statements
                | prog'''
    pass


def p_error(p):
    global validsyntax
    validsyntax = False
    if p is None:
        print ("Missing token")
    else:
        print(f"Syntax error at {p.value}")


parser = yacc.yacc() 
result = parser.parse(input_text)
if validsyntax:
    print("Valid syntax")
else:
    print("Invalid syntax")