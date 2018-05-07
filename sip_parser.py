import ply.yacc as yacc
import sip_lex as siplex
# from scipy import stats
# import matplotlib as mat
import os
import numpy
import sys
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
    print(p[1])

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
    print(p[1])

    if len(p) > 2:
        p[0] = (p[1], p[2], p[3])
    else:
        p[0] = p[1]


def p_block_method(p):
    '''block_method : method_np
                | method_1p
                | method_2p'''
    p[0] = p[1]

def p_method_list(p):
    '''method_list : block_method
                     | method_list'''
    if len(p) > 2:
        p[0] = (p[1], p[3])
    # else:
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
    p[0] = (p[1],p[2],p[3])
    print('Method with no parameters')


def p_method_1p(p):
    '''method_1p : METHOD_1P LP DIRECTION RP
                   | METHOD_1P LP LEVEL RP
                   | METHOD_1P LP STRING RP'''
    p[0] = (p[1], p[2], p[3], p[4])
    print('Method with 1 parameter')

def p_method_2p(p):
    '''method_2p : METHOD_2P LP INT COMMA INT RP '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6])
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

    if p[3][0] == "readImage":
        print("Hllo")
    # images[p[1]] = p[3]
    print('Method Assignment')

def p_SIP_method_block(p):
    '''SIP_method_block : ID LCB  method_list RCB '''
    p[0] = p[3]
    print(p[3])
    print('Method Block')

def p_empty(p):
    '''empty :  '''
    p[0] = None

def p_error(p):
    sys.exit("Syntax error in input")


def getparser():
    return yacc.yacc()

