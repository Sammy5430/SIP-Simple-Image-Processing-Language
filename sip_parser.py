import ply.yacc as yacc
import sip_lex as siplex
# from scipy import stats
import os
import numpy as np
import sys
from scipy.signal import convolve2d
import matplotlib.pylab as plt
import matplotlib.image as mpimg
# from skimage import feature (for now)
from scipy import ndimage
import re
from SIPAlgorithms import grayscale
from SIPAlgorithms import red
from SIPAlgorithms import blue
from SIPAlgorithms import green


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
                    | empty
                   '''
    p[0] = p[1]
    print('SIP Statement: {0}'.format(p[0]))

def p_assignment(p):
    '''assignment : img_assignment
                  | method_assignment
                    '''
    p[0] = p[1]
    print('Assignment: {0}'.format(p[0]))

def p_method(p):
    '''method : method_np
                | method_1p
                | method_2p
                | method_no'''

    p[0] = p[1]
    print('Method: {0}'.format(p[0]))

def p_method_no(p):
    '''method_no : METHOD_NO LP STRING RP '''
    #'METHOD_NO': ['read']
    p[0] = (p[1],p[3])
    print('Method No Object: {0}'.format(p[0]))

def p_method_np(p):
    '''method_np : ID DOT METHOD_NP LP RP '''
    # 'METHOD_NP': ['greyScale', 'sepia', 'red','green', 'blue', 'edges', 'segmentation', 'show'],
    p[0] = (p[3],p[1])

    if p[3] == 'greyscale':
        print("GreyScale")
        images[p[1]] = grayscale(images[p[1]])
        plt.imshow(images[p[1]],cmap="gray")
        # Remove ticks from axis
        plt.gca().get_xaxis().set_visible(False)
        plt.gca().get_yaxis().set_visible(False)
        plt.show()
    elif p[3] == "show":
        print('Executing Show')
        plt.imshow(images[p[1]])
        # Remove ticks from axis
        plt.gca().get_xaxis().set_visible(False)
        plt.gca().get_yaxis().set_visible(False)
        plt.show()
    elif p[3] == "red":
        print('Executing Red')
        images[p[1]] = red(images[p[1]])
        plt.imshow(images[p[1]])
        # Remove ticks from axis
        plt.gca().get_xaxis().set_visible(False)
        plt.gca().get_yaxis().set_visible(False)
        plt.show()
    elif p[3] == "blue":
        print('Executing Blue')
        images[p[1]] = blue(images[p[1]])
        plt.imshow(images[p[1]])
        # Remove ticks from axis
        plt.gca().get_xaxis().set_visible(False)
        plt.gca().get_yaxis().set_visible(False)
        plt.show()
    elif p[3] == "green":
        print('Executing Green')
        images[p[1]] = green(images[p[1]])
        plt.imshow(images[p[1]])
        # Remove ticks from axis
        plt.gca().get_xaxis().set_visible(False)
        plt.gca().get_yaxis().set_visible(False)
        plt.show()
    print('Method No Parameter: {0}'.format(p[0]))

def p_method_1p(p):
    '''method_1p : ID DOT METHOD_1P LP DIRECTION RP
                   | ID DOT METHOD_1P LP LEVEL RP
                   | ID DOT METHOD_1P LP STRING RP'''
    # 'METHOD_1P': ['enhance', 'sharpen', 'blur', 'denoise', 'rotate'],
    global images
    p[0] = (p[3], p[5])

    print('Method 1 Parameter: {0}'.format(p[0]))

def p_method_2p(p):
    '''method_2p : ID DOT METHOD_2P LP INT COMMA INT RP '''
    #'METHOD_2P': ['translate', 'resize'],
    p[0] = (p[3], p[5],p[7])
    print('Method 2 Parameter: {0}'.format(p[0]))


def p_img_assignment(p):
    '''img_assignment : ID EQUALS ID'''
    p[0] = (p[2], p[1], p[3])
    # global images
    images[p[1]] = p[3]
    print('IMG Assignment: {0}'.format(p[0]))

def p_method_assignment(p):
    '''method_assignment : ID EQUALS method_no'''
    p[0] = (p[2], p[1], p[3])
    global images
    print(p[0])
    if p[3][0] == "read":
        # Need to use the replace method to remove quotes from string
        path = p[3][1].replace('"', '')
        images[p[1]] = plt.imread(path)
        plt.imshow(images[p[1]])
        # Remove ticks from axis
        plt.gca().get_xaxis().set_visible(False)
        plt.gca().get_yaxis().set_visible(False)
        plt.show()
    print('Method Assignment: {0}'.format(p[0]))

def p_empty(p):
    '''empty :  '''
    p[0] = None

def p_error(p):
    sys.exit("Syntax error in input")


def getparser():
    return yacc.yacc()

