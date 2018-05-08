import ply.yacc as yacc
import sip_lex as siplex
# from scipy import stats
import os
import numpy as np
import sys
from scipy.signal import convolve2d
import matplotlib.pylab as plt
# from skimage import feature (for now)
from scipy import ndimage
import re


tokens = siplex.tokens

#sip variables:
images = {}

#need to add special bracket format

# ===========================================================================================
# Parsing rules
# ===========================================================================================

def p_statement(p):
    '''statement : method
                    | assignment
                    | SIP_method_block
                    | empty
                   '''
    p[0] = p[1]
    print(p[0])
    print('Origin')

    if p[0] == 'SIP':
        print("Hi")

def p_assignment(p):
    '''assignment : img_assignment
                  | method_assignment
                    '''
    p[0] = p[1]

def p_method(p):
    '''method : ID DOT method_np
                | ID DOT method_1p
                | ID DOT method_2p
                | method_no'''

    # if len(p) > 2:
    #     p[0] = (p[1], p[3])
    #     print("Hello")
    #     print(p[0])
    #     print("Hello")
    # else:
    #     p[0] = p[1]


def p_block_method(p):
    '''block_method : method_np
                | method_1p
                | method_2p'''
    p[0] = p[1]


def p_method_list(p):
    '''method_list : block_method
                     | block_method method_list'''

    if len(p) == 2:
        p[0] = p[1]
        print(len(p))
        print(p[0])
    elif len(p) == 3:
        p[0] = (p[1], p[2])
        print(len(p))
        print(p[0])
        print('hello')
    elif len(p) == 4:
        p[0] = (p[1], p[2], p[3])
        print(len(p))
        print(p[0])
    else:
        print('Method List')
        p[0] = p[1]


def p_method_no(p):
    '''method_no : METHOD_NO LP STRING RP '''
    # p[0] = (p[1], p[2], p[3], p[4])
    p[0] = (p[1],p[3])
    if p[1] == "readImage":
       print('Method with no object')


def p_method_np(p):
    '''method_np : METHOD_NP LP RP '''
    p[0] = p[1]
    print('Method with no parameters')


def p_method_1p(p):
    '''method_1p : METHOD_1P LP DIRECTION RP
                   | METHOD_1P LP LEVEL RP
                   | METHOD_1P LP STRING RP'''
    p[0] = (p[1], p[3])
    print(p[0])
    if p[1] == "show":
        print(p[0])
    print('Method with 1 parameter')

def p_method_2p(p):
    '''method_2p : METHOD_2P LP INT COMMA INT RP '''
    p[0] = (p[1], p[3], p[5])
    print('Method with two parameters')


def p_img_assignment(p):
    '''img_assignment : ID EQUALS ID'''
    # if isinstance((p[1], p[2], p[3]), image):
    p[0] = (p[1], p[2], p[3])
    # global images
    # images[p[1]] = p[3]
    print('IMG Assignment')

def p_method_assignment(p):
    '''method_assignment : ID EQUALS method'''
    p[0] = (p[1], p[2], p[3])
    global images
    print(p[0])
    if p[3][0] == "readImage":
        images[p[1]] = plt.imread(p[3][1].replace('"', '')) # Need to use the replace method to remove quotes from string
    print('Method Assignment')

def p_SIP_method_block(p):
    '''SIP_method_block : ID LCB  method_list RCB '''
    p[0] = ('SIP', p[1], p[3])
    print(p[3])
    print('Method Block')

def p_empty(p):
    '''empty :  '''
    p[0] = None

def p_error(p):
    sys.exit("Syntax error in input")


def getparser():
    return yacc.yacc()

