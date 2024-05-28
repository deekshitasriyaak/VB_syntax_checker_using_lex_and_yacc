import ply.yacc as yacc
from mkdir_lex import tokens
validsyntax=True

def p_statement(p):
    '''statement : MKDIR PATH'''
    global validsyntax
    validsyntax = True
def p_error(p):
    global validsyntax
    validsyntax = False
    print(f"Syntax error at {p.value}")

parser = yacc.yacc()
input_text = """MkDir Path"""

parser.parse(input_text)

if validsyntax:
    print("Valid Syntax")
else:
    print("Invalid Syntax")