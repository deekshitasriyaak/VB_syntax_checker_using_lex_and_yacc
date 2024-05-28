import ply.yacc as yacc
from var_decl_lex import input_text
tokens = ('DIM', 'VARI', 'COMMA', 'AS', 'DTYPE', 'SDTYPE')
validsyntax=True
def p_statement(p):
    '''statement : DIM parttwo'''
    global validsyntax
    validsyntax = True

def p_parttwo(p):
   '''parttwo : parttwo COMMA parttwo
            | partthree'''
   pass
   
def p_partthree(p):
    '''partthree : varlist asdt
                | VARI SDTYPE'''
    pass

def p_asdt(p):
   '''asdt : AS DTYPE'''
   pass

def p_varlist(p):
   '''varlist : VARI 
            | VARI COMMA varlist'''
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