import ply.yacc as yacc
from if_lex import input_text, tokens
validsyntax=True
def p_prog(p):
    '''prog : IF conds THEN STATEMENTS
            | IF conds THEN STATEMENTS ELSE STATEMENTS
            | IF conds THEN NEWLINE stats END IF
            | IF conds THEN NEWLINE stats ELSE stats END IF
            | IF conds THEN NEWLINE stats ELSEIF conds THEN stats END IF
            | IF conds THEN NEWLINE stats ELSEIF conds THEN stats ELSE stats END IF
    '''
    global validsyntax
    validsyntax = True


def p_conds(p):
    '''conds : STATEMENTS
            | conds AND conds
            | conds OR conds
            | conds conds'''
    pass

def p_stats(p):
    '''stats : STATEMENTS 
            | STATEMENTS NEWLINE 
            | NEWLINE
            | stats stats
            '''
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