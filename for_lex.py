import ply.lex as lex

tokens = (
    'FOR', 'EQUALS', 'NUMBER', 'TO', 'STEP', 'NEXT', 'EXIT', 'STATEMENTS'
)

t_TO = r'To'
t_EQUALS = r'='
t_STEP=r'Step'

def t_FOR(t):
    r'For'
    if t.value == 'For':
        t.type = 'FOR' 
    return t 
def t_EXIT(t):
    r'Exit For'
    if t.value == 'Exit':
        t.type = 'EXIT' 
    return t 
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STATEMENTS(t):
    r'[^ ]+' 
    if t.value == 'To':
        t.type = 'TO'  
    elif t.value == 'Step':
        t.type = 'STEP'  
    elif t.value=='Exit':
        t.type='EXIT'
    elif t.value == 'Next':
        t.type = 'NEXT' 
    elif t.value == 'For':
        t.type = 'FOR' 
    elif t.value=='=':
        t.type="EQUALS"
    return t

t_ignore = ' \t\n[]'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1) 

lexer = lex.lex()

input_text = """
For j = 1 To 10 Step 2
Next j=j+1"""

lexer.input(input_text)

for token in lexer:
    print(token)
