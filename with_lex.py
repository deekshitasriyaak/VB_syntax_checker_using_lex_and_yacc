import ply.lex as lex
tokens = ('WITH', 'STATEMENTS', 'END', 'NEWLINE', 'TERM')
t_WITH = r'With'
t_END = r'End'
t_NEWLINE = r'\n'
def t_STATEMENTS(t):
    r'[.][.a-zA-Z0-9_":; ()/]*[=][.a-zA-Z0-9_":; ()/]* | [.][.a-zA-Z0-9_":; ()/]*[()]'
    if t.value == 'End':
        t.type = 'END'  
    elif t.value == 'With':
        t.type = 'WITH'
    return t

def t_TERM(t):
    r'[.a-zA-Z_][.a-zA-Z0-9_]*'
    if t.value == 'End':
        t.type = 'END'  
    elif t.value == 'With':
        t.type = 'WITH'
    return t

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1) 

lexer = lex.lex() 

#valid
'''input_text = """With theCustomer
        .Name = "Coho Vineyard"
        .URL = "http://www.cohovineyard.com/"
        .City = "Redmond"
    End With""" '''


#invalid

input_text = '''With theCustomer
        .Name = "Coho Vineyard"
        .URL = "http://www.cohovineyard.com/"
        .City = "Redmond"
    End '''

lexer.input(input_text)

for token in lexer:
    print(token) 