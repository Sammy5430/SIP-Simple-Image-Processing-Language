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



def p_img_assignment(p):
    '''assignment : ID '=' ID'''
    # p[0] = p[1]
    # global images
    # images[p[1]] = p[3]
    print("hola")


def p_error(p):
    sys.exit("Sintax error in input")


def getparser():
    return yacc.yacc()

