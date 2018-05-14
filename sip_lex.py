# -----------------------------------------------------------------------------
# sip_lex.py
# SIP - Simple Image Processing Language
# -----------------------------------------------------------------------------
import ply.lex as lex
import ply.yacc as yacc
from ply.lex import TOKEN
import re
import sys

# reserved Words

reserved = {
    'METHOD_NP': ['grayscale', 'sepia', 'red',
                  'green', 'blue', 'show','sharpen','invert'],
    'METHOD_1P': ['blur', 'rotate','edges', 'save'],
    'METHOD_2P': ['translate', 'resize','crop','spiral'],
    'METHOD_NO': ['read'],
    'LEVEL': ['low', 'medium', 'high'],
    'DIRECTION': ['right', 'left'],
}

# tokens
tokens = [
    'INT',
    'EQUALS', 'ID', 'DOT',
    'COMMA', 'LP', 'RP', 'STRING',
] + list(reserved)

# print(tokens)

# Declaration of Basic Regular Expressions
t_EQUALS = r'\='
t_DOT = r'\.'
t_COMMA = r'\,'
t_LP = r'\('
t_RP = r'\)'

# SIP Regular Expressions Patterns
reg_method_np = re.compile('|'.join(reserved['METHOD_NP']))
reg_method_1p = re.compile('|'.join(reserved['METHOD_1P']))
reg_method_2p = re.compile('|'.join(reserved['METHOD_2P']))
reg_method_no = re.compile(reserved.get('METHOD_NO')[0])
reg_level = re.compile('|'.join(reserved['LEVEL']))
reg_direction = re.compile('|'.join(reserved['DIRECTION']))

# SIP Regular Expressions
@TOKEN(reg_method_np.pattern)
def t_METHOD_NP(t):
    return t


@TOKEN(reg_method_1p.pattern)
def t_METHOD_1P(t):
    return t


@TOKEN(reg_method_2p.pattern)
def t_METHOD_2P(t):
    return t


@TOKEN(reg_method_no.pattern)
def t_METHOD_NO(t):
    return t


@TOKEN(reg_level.pattern)
def t_LEVEL(t):
    return t


@TOKEN(reg_direction.pattern)
def t_DIRECTION(t):
    return t

# Generic Regular Expressions

def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_STRING(t):
    r'\"(.+?)\"'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'ID'
    # t.type = reserved.get(t.value, 'ID')  # Check reserved words
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
lexer = lex.lex(reflags=re.UNICODE)
#

# test1 = "img.rotate(right)"
# test2 = "hello = readImage(\"Desktop\")"
#
# lexer.input(test2)


# Looping for input
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)
