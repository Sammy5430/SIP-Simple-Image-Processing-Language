import numpy as np
from scipy.signal import convolve2d
import matplotlib.pylab as plt
from skimage import feature
from scipy import ndimage

def sharpen(im):
    #Create the identity filter, but with the 1 shifted to the right!
    kernel = np.zeros( (9,9), np.float)
    k = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    kernel[4,4] = 2.00   #Identity, times two! 

    #Create a box filter:
    boxFilter = np.ones( (9,9), np.float) / 81.0

    #Subtract the two:
    kernel = kernel - boxFilter

    #Note that we are subject to overflow and underflow here...but I believe that
    # filter2D clips top and bottom ranges on the output, plus you'd need a
    # very bright or very dark pixel surrounded by the opposite type.

    #custom = cv2.filter2D(imgIn, -1, kernel)
    """blurred_f = gaussian(im, "MEDIUM")
    filter_blurred_f = gaussian(blurred_f, 1)
    alpha = 60
    sharpened = im + alpha * (im - blurred_f)"""
    sharpened = _convolve_all_colours(im, k)
    return sharpened

def canny(im, level):
    intensity = {'HIGH':1, 'MEDIUM':3, "LOW":6 }
    edges = feature.canny(gray, sigma=intensity[level])
    return edges

def _convolve_all_colours(im, window):
    """
    Convolves im with window, over all three colour channels
    """
    ims = []
    for d in range(3):
        im_conv_d = convolve2d(im[:,:,d], window, mode="same", boundary="symm")
        ims.append(im_conv_d)

    im_conv = np.stack(ims, axis=2).astype("uint8")
    return im_conv

def gaussian(im, level, size = 13):
    intensity = {'HIGH':(65,17), 'MEDIUM':(33,13), 'LOW':(9,9) }
    try:
        sigma = intensity[level][0]
        n = intensity[level][1]
    except Exception:
        sigma = level
        n = size
    nn = int((n-1)/2)
    a = np.asarray([[x**2 + y**2 for x in range(-nn,nn+1)] for y in range(-nn,nn+1)])
    gauss_win = np.exp(-a/(2*sigma**2))
    gauss_win /= np.sum(gauss_win)
    return _convolve_all_colours(im, gauss_win)



def simple_threshold(im, threshold=128):
    return ((im > threshold) * 255).astype("uint8")
    
def plti(im, h=8, **kwargs):
    """
    Helper function to plot an image.
    """
    y = im.shape[0]
    x = im.shape[1]
    w = (y/x) * h
    plt.figure(figsize=(w,h))
    plt.imshow(im, interpolation="none", **kwargs)
    plt.axis('off')


def grayscale(im, weights = np.c_[0.2989, 0.5870, 0.1140]):
    return np.dot(im[...,:3], [0.299, 0.587, 0.114])

def otsu_threshold(im):

    pixel_counts = [np.sum(im == i) for i in range(256)]

    s_max = (0,-10)
    ss = []
    for threshold in range(256):

        # update
        w_0 = sum(pixel_counts[:threshold])
        w_1 = sum(pixel_counts[threshold:])

        mu_0 = sum([i * pixel_counts[i] for i in range(0,threshold)]) / w_0 if w_0 > 0 else 0       
        mu_1 = sum([i * pixel_counts[i] for i in range(threshold, 256)]) / w_1 if w_1 > 0 else 0

        # calculate 
        s = w_0 * w_1 * (mu_0 - mu_1) ** 2
        ss.append(s)

        if s > s_max[1]:
            s_max = (threshold, s)
            
    return s_max[0]

def threshold(im):
    pixel_counts = [np.sum(im == i) for i in range(256)]

    s_max = (0,-10)
    ss = []
    for threshold in range(256):

        # update
        w_0 = sum(pixel_counts[:threshold])
        w_1 = sum(pixel_counts[threshold:])

        mu_0 = sum([i * pixel_counts[i] for i in range(0,threshold)]) / w_0 if w_0 > 0 else 0       
        mu_1 = sum([i * pixel_counts[i] for i in range(threshold, 256)]) / w_1 if w_1 > 0 else 0

        # calculate 
        s = w_0 * w_1 * (mu_0 - mu_1) ** 2
        ss.append(s)

        if s > s_max[1]:
            s_max = (threshold, s)
            
    thresh = s_max[0]
    return ((im > thresh) * 255).astype("uint8")

im = plt.imread("DT.jpg")
gray = gaussian(im, 'LOW')
plt.imshow(gray)
#sharp = canny(im, 'LOW')
#plt.imshow(sharp, cmap='gray')
#plt.imshow(sharp)
"""
plti(sharpen(im))
gray_im = to_grayscale(im)
t = otsu_threshold(gray_im)
plti(simple_threshold(gray_im, t), cmap='Greys')"""
plt.show()
