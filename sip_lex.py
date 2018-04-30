# -----------------------------------------------------------------------------
#sip_lex.py
#SIP - Simple Image Processing Language
#
# -----------------------------------------------------------------------------
import ply.lex as lex
import ply.yacc as yacc
import sys

#reserved Words
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

#tokens
tokens = (
    'INT', 'FLOAT',
    'EQUALS', 'ID', 'LBRACE', 'RBRACE', 'EQUALS', 'DOT',
    'COMMA','LPAREN', 'RPAREN', 'STRING'
)

#Basic Regular Expressions
t_EQUALS = r'\='
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DOT    = r'\.'
t_COMMA  = r'\,'
t_LPAREN = r'\('
t_RPAREN = r'\)'




