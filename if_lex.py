import ply.lex as lex
"""
' Multiline syntax:
If condition [ Then ]
    [ statements ]
[ ElseIf elseifcondition [ Then ]
    [ elseifstatements ] ]
[ Else
    [ elsestatements ] ]
End If

' Single-line syntax:
If condition Then [ statements ] [ Else [ elsestatements ] ]
"""

tokens = ('IF','THEN','ELSEIF','ELSE','END', 'STATEMENTS', 'OR','AND', 'NEWLINE')
t_IF = r'If'
t_THEN = r'Then'
t_ELSEIF = r'ElseIf'
t_ELSE = r'ELSE'
t_END = r'End'
t_OR = r'Or'
t_AND = r'And'
t_NEWLINE = r'\n'


def t_STATEMENTS(t):
    r'[^ \n]+'
    if t.value == 'If':
        t.type = 'IF'  
    elif t.value == 'Then':
        t.type = 'THEN'
    elif t.value == 'ElseIf':
        t.type = 'ELSEIF'
    elif t.value == 'Else':
        t.type = 'ELSE'
    elif t.value == 'End':
        t.type = 'END'
    elif t.value == 'And':
        t.type = 'AND'
    elif t.value == 'Or':
        t.type = 'OR'
    return t


t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1) 

lexer = lex.lex() 

#valid
input_text = '''If count = 0 Then
    message = "There are no items."
    'If count is 1, output will be "There is 1 item.".        
ElseIf count = 1 Then
    message = "There is 1 item."
    'If count is greater than 1, output will be "There are {count} items.", where {count} is replaced by the value of count. 
Else
    message = $"There are {count} items."
End If'''


#invalid
"""input_text = '''If count = 0 Then
    message = "There are no items."
    'If count is 1, output will be "There is 1 item.".        
ElseIf count = 1 Then Then
    message = "There is 1 item."
    'If count is greater than 1, output will be "There are {count} items.", where {count} is replaced by the value of count. 
Else
    message = $"There are {count} items."
End If'''"""

lexer.input(input_text)

for token in lexer:
    print(token) 
