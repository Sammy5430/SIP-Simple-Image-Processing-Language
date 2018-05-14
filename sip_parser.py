import ply.yacc as yacc
import sip_lex as siplex
import sys
import matplotlib.pylab as plt
import numpy as np
from SIPAlgorithms import grayscale
from SIPAlgorithms import red
from SIPAlgorithms import blue
from SIPAlgorithms import green
from SIPAlgorithms import sepia
from SIPAlgorithms import rotate
from SIPAlgorithms import gaussian
from SIPAlgorithms import sharpen
# from SIPAlgorithms import sharpen2
from SIPAlgorithms import re_size
from SIPAlgorithms import canny
from SIPAlgorithms import imshow
from SIPAlgorithms import imread
from SIPAlgorithms import invert
from SIPAlgorithms import crop
from SIPAlgorithms import spiral
from SIPAlgorithms import saveimg
from SIPAlgorithms import isgray

tokens = siplex.tokens

global image_path, current_image

#sip variables:
images = {}

# ===========================================================================================
# Parsing rules
# ===========================================================================================

def p_statement(p):
    '''statement : method
                    | assignment
                    | empty
                   '''

    p[0] = p[1]
    # print('SIP Statement: {0}'.format(p[0]))

def p_assignment(p):
    '''assignment : img_assignment
                  | method_assignment
                    '''
    p[0] = p[1]
    # print('Assignment: {0}'.format(p[0]))

def p_method(p):
    '''method : method_np
                | method_1p
                | method_2p
                | method_no'''

    p[0] = p[1]
    # print('Method: {0}'.format(p[0]))

def p_method_no(p):
    '''method_no : METHOD_NO LP STRING RP '''

    if p[1].lower() == "readImage".lower():
        # image_path = p[3]
        # current_image = cv2.imread(image_path)
        print("Image uploaded")

    p[0] = (p[1],p[3])
    # print('Method No Object: {0}'.format(p[0]))

def p_method_np(p):
    '''method_np : ID DOT METHOD_NP LP RP '''


    p[0] = (p[3],p[1])
    global images

    if images.get(p[1]) is None:
        print("ID Error")
        return p

    copy = images[p[1]].copy()
    if p[3] == 'grayscale':
        # print("GrayScale")
        if isgray(copy):
            print("Can't call this method on a 2D image.")

        else:
            copy = grayscale(copy)
            imshow(copy)
            plt.show()

    elif p[3] == "sepia":
        # print("Sepia")
        if isgray(copy):
            print("Can't call this method on a 2D image.")

        else:
            copy = sepia(copy)
            imshow(copy)
            plt.show()

    elif p[3] == "show":
        # print('Executing Show')
        imshow(copy)
        plt.show()

    elif p[3] == "red":
        # print('Executing Red')
        if isgray(copy):
            print("Can't call this method on a 2D image.")

        else:
            copy = red(copy)
            imshow(copy)
            plt.show()

    elif p[3] == "blue":
        # print('Executing Blue')
        if isgray(copy):
            print("Can't call this method on a 2D image.")

        else:
            copy = blue(copy)
            imshow(copy)
            plt.show()

    elif p[3] == "green":
        # print('Executing Green')
        if isgray(copy):
            print("Can't call this method on a 2D image.")

        else:
            copy = green(copy)
            imshow(copy)
            plt.show()

    elif p[3] == 'sharpen':
        # print('Sharpen')
        copy = sharpen(copy)
        imshow(copy)
        plt.show()

    elif p[3] == 'invert':
        copy = invert(copy)
        imshow(copy)
        plt.show()

    if not np.array_equal(copy, images[p[1]]):
        changes = input("Keep Changes? (y/n):")
        if changes == "y":
            images.update({p[1]: copy})
        else:
            return p

    # print('Method No Parameter: {0}'.format(p[0]))

def p_method_1p(p):
    '''method_1p : ID DOT METHOD_1P LP DIRECTION RP
                   | ID DOT METHOD_1P LP LEVEL RP
                   | ID DOT METHOD_1P LP STRING RP'''

    global images
    if images.get(p[1]) is None:
        print("ID Error")
        return p

    copy = images[p[1]].copy()

    p[0] = (p[3], p[5])

    if p[3] == 'blur':
        # print('Blur')
        if isgray(copy):
            print("Can't call this method on a 2D image.")

        else:
            copy = gaussian(copy, p[5])
            imshow(copy)
            plt.show()

    elif p[3] == 'rotate':
        # print('Rotate')
        copy = rotate(copy, p[5])
        imshow(copy)
        plt.show()

    elif p[3] == 'edges':
        # print('Edges')
        if isgray(copy):
            copy = canny(copy, p[5])
            imshow(copy)
            plt.show()

        else:
            print("Can't call this method on a 3D image.")

    elif p[3] == 'save':
        # print('Edges')
        saveimg(copy, p[5].replace('"', ''))

    if not np.array_equal(copy, images[p[1]]):
        changes = input("Keep Changes? (y/n):")
        if changes == "y":
            images.update({p[1]: copy})
        else:
            return p

        # print('Method 1 Parameter: {0}'.format(p[0]))

def p_method_2p(p):
    '''method_2p : ID DOT METHOD_2P LP INT COMMA INT RP
                 | ID DOT METHOD_2P LP ID COMMA STRING
                 '''
    #'METHOD_2P': ['translate', 'resize'],
    p[0] = (p[3], p[5],p[7])

    global images

    if images.get(p[1]) is None:
        print("ID Error")
        return p

    copy = images[p[1]].copy()

    if p[3] == 'translate':
        imshow(images[p[1]])
        plt.show()

    elif p[3] == 'resize':
        # print('Resize')
        copy = re_size(copy, p[5], p[7])
        imshow(copy)
        plt.show()

    elif p[3] == 'crop':
        copy = crop(copy, p[5], p[7])
        imshow(copy)
        plt.show()

    elif p[3] == 'spiral':
        copy = spiral(copy, p[5], p[7])
        imshow(copy)
        plt.show()

    changes = input("Keep Changes? (y/n):")
    if changes == "y":
        images.update({p[1]: copy})
    else:
        return p

    # print('Method 2 Parameter: {0}'.format(p[0]))


def p_img_assignment(p):
    '''img_assignment : ID EQUALS ID'''
    p[0] = (p[2], p[1], p[3])
    global images

    if images.get(p[3]) is not None:
        images[p[1]] = None
        images.update({p[1]:images[p[3]]})
    else:
        print('ID Error')
    # print('IMG Assignment: {0}'.format(p[0]))

def p_method_assignment(p):
    '''method_assignment : ID EQUALS method_no'''
    p[0] = (p[2], p[1], p[3])
    global images

    if p[3][0] == "read":
        # Need to use the replace method to remove quotes from string
        path = p[3][1].replace('"', '')
        temp = imread(path)
        if temp is None:
            print("Error: Image not Found")
            return p
        else:
            images[p[1]] = imread(path)
            imshow(images[p[1]])
            plt.show()
    else:
        print("Cannot use that method in a assignment")
    # print('Method Assignment: {0}'.format(p[0]))

def p_empty(p):
    '''empty :  '''
    p[0] = None

def p_error(p):
    print("SIP Syntax error")
    # sys.exit("Syntax error in input")


def getparser():
    return yacc.yacc()


