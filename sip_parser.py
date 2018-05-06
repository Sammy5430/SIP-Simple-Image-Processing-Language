import ply.yacc as yacc
import sip_lex as siplex
# from scipy import stats
# import matplotlib as mat
import os
import numpy
import sys
tokens = siplex.tokens
import cv2

#sip variables:
images = {}

# ===========================================================================================
# METHODS
# ===========================================================================================

def p_method(p):
    '''method : classifier
                | upload_methods
                | transf_methods
                | filtering_methods
                | color_methods
                | feature_extraction_methods
                | plotting_methods
                | special_method'''

    p[0] = p[1]

def p_upload_methods(t):
    '''upload_methods : UPLOAD_COMMAND '(' PATH ')' '''

    t[0] = t[1]
    t[3] = t[3][1:-1]

    if t[1].lower() == "uploadImage".lower():
        global imagePath, currentImage
        imagePath = t[3]
        currentImage = cv2.imread(imagePath)
        print("Image uploaded")

def p_tranf_methods(t):
    '''transf_methods : TRANSFORM_COMMAND '(' FLOAT, FLOAT ')'
                        | TRANSFORM_COMMAND '(' ID ')' '''

    t[0] = t[1]
    t[3] = t[3][1:-1]

    if len(t) > 3 and isinstance(t[3], float):
        if t[1].lower() == "resize".lower():
            # Insert resize method below
            pass #comment this when done

        if t[1].lower() == "translate".lower():
            # Insert translate method below
            pass  # comment this when done

    if len(t) > 2 and isinstance(t[3], str):
        if t[1].lower() == "rotate".lower():
            # Insert rotate method below
            pass  # comment this when done

def p_filtering_methods(t):
    '''filtering_methods : FILTERING_COMMAND '(' STRING ')' '''

    t[0] = t[1]
    t[3] = t[3][1:-1]

    if len(t) > 2 and isinstance(t[3], str) and (t[3] == "medium" or t[3] == "low" or t[3] == "high"):
        if t[1].lower() == "enhance".lower():
            # Insert enhance method below
            pass  # comment this when done

        if t[1].lower() == "sharpen".lower():
            # Insert sharpen method below
            pass  # comment this when done

        if t[1].lower() == "blur".lower():
            # Insert blur method below
            pass  # comment this when done

        if t[1].lower() == "denoise".lower():
            # Insert denoise method below
            pass  # comment this when done

def p_color_methods(t):
    '''color_methods : COLOR_COMMAND '(' ')' ''' #ADD TINT METHOD IF DECIDED TO DO SO

    t[0] = t[1]

    if t[1].lower() == "greyScale".lower():
        # Insert greyscale method below
        pass  # comment this when done

    if t[1].lower() == "sepia".lower():
        # Insert sepia method below
        pass  # comment this when done

    if t[1].lower() == "getR".lower():
        # Insert getR method below
        pass  # comment this when done

    if t[1].lower() == "getG".lower():
        # Insert getG method below
        pass  # comment this when done

    if t[1].lower() == "getB".lower():
        # Insert getB method below
        pass  # comment this when done

def p_feature_extraction_methods(t):
    '''feature_extraction_methods : FEATURE_EXTRACTION_COMMAND '(' ')' '''

    t[0] = t[1]

    if t[1].lower() == "getEdges".lower():
        # Insert getEdges method below
        pass  # comment this when done

    if t[1].lower() == "segmentation".lower():
        # Insert segmentation method below
        pass  # comment this when done

def p_plotting_methods(t):
    '''plotting_methods : PLOTTING_COMMAND '(' ID ')' ''' # ID or string?

    t[0] = t[1]

    if len(t) > 3:
        if t[1].lower() == "show".lower():
            # Insert show method with title parameter below
            pass  # comment this when done

    else:
        if t[1].lower() == "show".lower():
            # Insert show method without title parameter below
            pass  # comment this when done

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
    if len(p) >= 2:
        p[0] = (p[1], p[2], p[3])
    else:
        p[0] = p[1]


def p_block_method(p):
    '''block_method : method_np
                | method_1p
                | method_2p'''
    # p[0] = p[1]

def p_method_list(p):
    '''method_list : block_method
                     | method_list'''
    if len(p) > 2:
        p[0] = (p[1], p[3])
    else:
        p[0] = p[1]


def p_method_no(p):
    '''method_no : METHOD_NO LP STRING RP '''
    p[0] = (p[1],p[2],p[3],p[4])
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
    # global images
    # images[p[1]] = p[3]
    print('Method Assignment')

def p_SIP_method_block(p):
    '''SIP_method_block : ID LCB  method_list RCB '''
    p[0] = p[3]
    print('Method Block')

def p_empty(p):
    '''empty :  '''
    p[0] = None

def p_error(p):
    sys.exit("Syntax error in input")


def getparser():
    return yacc.yacc()

