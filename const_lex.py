
import ply.lex as lex

# Define the tokens
tokens = (
    'PUBLIC',
    'PRIVATE',
    'CONST',
    'AS',
    'DTYPE',
    'EQUALS',
    'NUM',
    'VAR',
    'STRING',
    'COMMA'
)

# Define regular expressions for tokens
t_PUBLIC = r'Public'
t_PRIVATE = r'Private'
t_CONST = r'Const'
t_AS = r'As'
t_STRING=r'[a-zA-Z_][a-zA-Z0-9_]*'

# Define a rule for data types
def t_DTYPE(t):
    r'Integer|Long|Short|Byte|Single|Double|Decimal|String|Boolean|Date|Object|Char|Variant|Currency'
    return t

def t_NUM(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value == 'Public':
        t.type = 'PUBLIC'
    elif t.value == 'Private':
        t.type = 'PRIVATE'
    elif t.value == 'Const':
        t.type = 'CONST'
    elif t.value=='As':
        t.type='AS'
    return t

t_EQUALS = r'='
t_ignore = ' \t"'
t_COMMA=r','
# Define a rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test your lexer with input code
input_text = """
Const conAge As Integer = 34
"""

lexer.input(input_text)
for token in lexer:
    print(token)
