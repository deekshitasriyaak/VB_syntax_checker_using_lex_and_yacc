"""
syntax for variable declaration, gen format:
1. Dim {var} As {datatype}
2. Dim {var1, var2, var3 etc} As {Datatype}
3. Dim {var1} As {datatype}, {var2} As {Datatype} , {var3} ... etc
4. Dim {var1}{short form for datatype}
5. Dim {var1}{short form for datatype}, {var2}{short form for datatype}, ..., {var3} As {datatype} ...
{} not included
"""
import ply.lex as lex

tokens = ('DIM', 'VARI', 'COMMA', 'AS', 'DTYPE', 'SDTYPE')

t_DIM = r'Dim'
t_COMMA = r','
t_AS = r'As'

def t_DTYPE(t):
    r'Integer|Long|Short|Byte|Single|Double|Decimal|String|Boolean|Date|Object|Char|Variant|Currency'
    return t


def t_VARI(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value == 'Dim' or t.value == 'Public' or t.value == 'Private':
        t.type = 'DIM'  
    elif t.value == 'As':
        t.type = 'AS'
    return t

def t_SDTYPE(t):
    r'%|@|&|\#|!|\$'
    return t


t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1) 

lexer = lex.lex() 


#valid

input_text = '''Dim i As '''
#input_text = '''Dim i, j, k As Integer'''


#invalid

#input_text = '''i, Dim As Interger'''
#input_text = '''Dim i As Number'''

lexer.input(input_text)

for token in lexer:
    print(token) 