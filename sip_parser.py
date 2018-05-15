import ply.yacc as yacc
import sip_lex as siplex
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
                   | ID DOT METHOD_1P LP STRING RP
                   | ID DOT METHOD_1P LP INT RP'''

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

    elif p[3] == 'sharpen':
        # print('Sharpen')
        copy = sharpen(copy, p[5])
        imshow(copy)
        plt.show()

    elif p[3] == 'save':
        # print('Saving')
        path = p[5]
        valid = False
        while not valid:
            try:
                saveimg(copy, path.replace('"', ''))
                valid = True
            except:
                index = path.find('.')
                if index > 0:
                    path = path[ : index]
                extension = input("Please provide a valid file extension ('.jpg', '.jpeg', '.png'): ")
                path = path + extension

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

    if p[3] == 'resize':
        # print('Resize')
        if(p[5] >= 6000 or p[7] >= 6000):
            print("Higher resize values take a longer time to apply.")
        try:
            copy2 = re_size(copy, p[5], p[7])
            imshow(copy2)
            plt.show()
            copy = copy2
        except:
            if p[5] <= 0 or p[7] <= 0:
                print("Resize values must be higher than or equal to 1")

    elif p[3] == 'crop':
        width = copy.shape[1]
        height = copy.shape[0]
        if p[5] > width and p[7] > height:
            print("Given width  and height values exceed width and height of original image.")
            print("Valid width values for cropping the specified image are those between 1 and " + str(width))
            print("Valid height values for cropping the specified image are those between 1 and " + str(height))
        elif p[5] > width:
            print("Given width value exceeds width of original image.")
            print("Valid width values for cropping the specified image are those between 1 and " + str(width))
        elif p[7] > height:
            print("Given height value exceeds height of original image.")
            print("Valid height values for cropping the specified image are those between 1 and " + str(height))
        else:
            try:
                copy2 = crop(copy, p[5], p[7])
                imshow(copy2)
                plt.show()
                copy = copy2
            except:
                if p[5] == 0 or p[7] == 0:
                    print("Zero (0) is not a valid crop value for neither height nor width.")
                elif p[5 <= 0 or p[7] <= 0]:
                    print("Negative crop values are not valid for neither height nor width.")
                else:
                    print("Invalid crop parameters.")
                print("Valid width values for cropping the specified image are integers between 1 and " + str(width))
                print("Valid height values for cropping the specified image are integers between 1 and " + str(height))

    elif p[3] == 'spiral':
        if p[5] == 0 and p[7]==0:
            print("Providing a strength and rotation value of zero (0) will not change the image.")
        elif p[7] == 0:
            print("A rotation value of zero (0) will not generate any perceivable change.")
        elif p[5] == 0:
            print("A strength value of zero (0) will not generate any perceivable change.")
        elif p[5] < 0 or p[7] < 0:
            print("Negative values are not valid for the spiral method.")
        else:
            try:
                copy2 = spiral(copy, p[5], p[7])
                imshow(copy2)
                plt.show()
                copy = copy2
            except:
                print("Invalid parameters for spiral method.")

    if not np.array_equal(copy, images[p[1]]):
        changes = input("Keep Changes? (y/n):")
        if changes == "y":
            images.update({p[1]: copy})
            print("Changes to '" + str(p[1]) + "' were saved successfully.")
        else:
            print("Changes to '" + str(p[1]) + "' were discarded.")
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
        if not path.endswith(('.jpg', '.jpeg', '.png')):
            try:
                if(path.endswith('.')):
                    path = path +'jpg'
                else:
                    path = path + '.jpg'
                images[p[1]] = imread(path)
                imshow(images[p[1]])
                plt.show()
            except(Exception):
                try:
                    path = path[:-4]
                    if (path.endswith('.')):
                        path = path + 'jpeg'
                    else:
                        path = path + '.jpeg'
                    images[p[1]] = imread(path)
                    imshow(images[p[1]])
                    plt.show()
                except:
                    try:
                        path = path[:-4]
                        if (path.endswith('.')):
                            path = path + 'png'
                        else:
                            path = path + '.png'
                        images[p[1]] = imread(path)
                        imshow(images[p[1]])
                        plt.show()
                    except:
                        print("Error: Image Not Found")
                        return

        else:
            try:
                images[p[1]] = imread(path)
                imshow(images[p[1]])
                plt.show()
            except:
                print("Error: Image Not Found")

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


