# -----------------------------------------------------------------------------
# sip_lex.py
# SIP - Simple Image Processing Language
# -----------------------------------------------------------------------------
import ply.lex as lex
import ply.yacc as yacc
import sys

# reserved Words
reserved = {
    'readImage': 'READ',
    'rotate': 'ROTATE',
    'resize': 'RESIZE',
    'translate': 'TRANSLATE',
    'enhance': 'ENHANCE',
    'sharpen': 'SHARPEN',
    'blur': 'BLUR',
    'denoise': 'DENOISE',
    'greyScale': 'GREY',
    'sepia': 'SEPIA',
    'getR': 'RED',
    'getG': 'GREEN',
    'getB': 'BLUE',
    'getEdges': 'EDGES',
    'segmentation': 'SEGMENTATION',
    'show': 'SHOW'

}

# tokens
tokens = (
    'INT', 'FLOAT',
    'EQUALS', 'ID', 'LBRACE', 'RBRACE', 'EQUALS', 'DOT',
    'COMMA', 'LPAREN', 'RPAREN', 'STRING', 'METHOD'
)

# Basic Regular Expressions
t_EQUALS = r'\='
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DOT = r'\.'
t_COMMA = r'\,'
t_LPAREN = r'\('
t_RPAREN = r'\)'


# Regular Expression

def t_FLOAT(t):
    r'\d+\.\d'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'ID'
    return t

# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Lexer
lexer = lex.lex()

lexer.input("img.readImage()")

# Looping for input
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
