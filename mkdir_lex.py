import ply.lex as lex
tokens=(
    'MKDIR','PATH'
)

t_MKDIR=r'MkDir'
def t_PATH(t):
    r'[^ ]+' 
    if t.value == 'MkDir':
        t.type = 'MKDIR' 
    return t
t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1) 

lexer = lex.lex()

input_text = """MkDir Path"""

lexer.input(input_text)

for token in lexer:
    print(token)
