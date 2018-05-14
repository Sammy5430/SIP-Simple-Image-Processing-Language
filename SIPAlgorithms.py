import numpy as np
from scipy.signal import convolve2d
import matplotlib.pylab as plt
from skimage import feature
from scipy import ndimage
from scipy import misc
from skimage.transform import resize
from skimage.transform import swirl
from skimage.transform import rescale
from skimage import util
from skimage import io
from skimage import filters


def _convolve_all_colours(im, window):
    """
    Convolves im with window, over all three colour channels
    """
    ims = []
    for d in range(3):
        im_conv_d = convolve2d(im[:, :, d], window, mode="same", boundary="symm")
        ims.append(im_conv_d)

    im_conv = np.stack(ims, axis=2).astype("uint8")
    return im_conv


def _DynamicThreshold(im):
    """
        Goes through the pixels in an image and sets the threshold parameters
        based on the most prominent features.
    """
    pixel_counts = [np.sum(im == i) for i in range(256)]
    s_max = (0, -10)
    ss = []
    for threshold in range(256):

        w_0 = sum(pixel_counts[:threshold])
        w_1 = sum(pixel_counts[threshold:])

        mu_0 = sum([i * pixel_counts[i] for i in range(0, threshold)]) / w_0 if w_0 > 0 else 0
        mu_1 = sum([i * pixel_counts[i] for i in range(threshold, 256)]) / w_1 if w_1 > 0 else 0

        s = w_0 * w_1 * (mu_0 - mu_1) ** 2
        ss.append(s)

        if s > s_max[1]:
            s_max = (threshold, s)

    thresh = s_max[0]
    return ((im > thresh) * 255).astype("uint8")


def sharpen(im):
    sharpened = misc.imfilter(im, 'sharpen')
    return sharpened

def sharpen2(image, sigma=10):
    intesity = {'HIGH':(2, 0.6), 'MEDIUM':(1.3,0.3), 'LOW':(.6,.3)}
    a = 1.3
    b = 0.3
    blurred = filters.gaussian(image, sigma=sigma, multichannel=True)
    sharper = np.clip(image * a - blurred * b, 0, 1.0)
    return sharper


def canny(im, level):
    level = level.upper()
    intensity = {'HIGH': 1, 'MEDIUM': 3, "LOW": 6}
    edges = feature.canny(im, sigma=intensity[level])
    return edges


def gaussian(im, level, size=13):
    intensity = {'HIGH': (65, 17), 'MEDIUM': (33, 13), 'LOW': (9, 9)}
    level = level.upper()
    try:
        sigma = intensity[level][0]
        n = intensity[level][1]
    except Exception:
        sigma = level
        n = size
    nn = int((n - 1) / 2)
    a = np.asarray([[x ** 2 + y ** 2 for x in range(-nn, nn + 1)] for y in range(-nn, nn + 1)])
    gauss_win = np.exp(-a / (2 * sigma ** 2))
    gauss_win /= np.sum(gauss_win)
    return _convolve_all_colours(im, gauss_win)


def threshold(im, level):
    """
        Dynamic threshold if level is not given, else uses level to theshold the image.
    """
    level = level.upper()
    intensity = {'HIGH': 175, 'MEDIUM': 75, 'LOW': 25}
    if (level is None):
        img = _DynamicThreshold(im)
    else:
        try:
            img = ((im > intensity[level]) * 255).astype("uint8")
        except Exception:
            img = _DynamicThreshold(im)
    return img


def imshow(im, h=6):
    """
        Helper function to show an image.
    """
    y = im.shape[0]
    x = im.shape[1]
    w = (y / x) * h
    plt.figure(figsize=(w, h))
    if (len(im.shape) == 3):
        plt.imshow(im)
    else:
        plt.imshow(im, cmap='gray')
    plt.axis('off')


def imread(imageName):
    try:
        im = plt.imread(imageName)
        extension = imageName.split('.')[1]
        if (extension == 'png'):
            im = 255 * im
            im = im.astype(np.uint8)
            return im
        else:
            return im
    except Exception:
        print(Exception)


def grayscale(im, weights=np.c_[0.2989, 0.5870, 0.1140]):
    return np.dot(im[..., :3], [0.299, 0.587, 0.114])


def red(im):
    im[:, :, 1] = 0  # Zero out contribution from green
    im[:, :, 2] = 0  # Zero out contribution from blue
    return im


def blue(im):
    im[:, :, 1] = 0  # Zero out contribution from green
    im[:, :, 0] = 0  # Zero out contribution from red
    return im


def green(im):
    im[:, :, 0] = 0  # Zero out contribution from blue
    im[:, :, 2] = 0  # Zero out contribution from red
    return im


def sepia(im):
    sepia_filter = np.array([[.393, .769, .189],
                             [.349, .686, .168],
                             [.272, .534, .131]])

    sepia_img = im.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()

    return im

def rotate(im, direction):
    direction = direction.lower()

    d = {'right': -90, 'left': 90}
    # Default reshaping is true
    rim = ndimage.rotate(im, d[direction])
    return rim

def re_size(im, h, w):
    im = resize(im, (h, w),mode='constant')
    return im

def invert(im):
    return util.invert(im)

#Crop with respect to the center of the image, cropx and cropy cannot be larger that the dimesions of the image
def crop(im, cropx, cropy):
    y = im.shape[0]
    x = im.shape[1]
    startx = x // 2 - (cropx // 2)
    starty = y // 2 - (cropy // 2)
    return im[starty:starty + cropy, startx:startx + cropx]

#second parameter  is the strength of the spiral and third parameter is the radius of the spiral
def spiral(im, s, r):
    return swirl(im, center=None, strength=s, radius=r, rotation=0, output_shape=None, order=1,
                            mode='constant', cval=0, clip=True, preserve_range=False)

def re_scale(im, factor):
    return rescale(im, factor, order=1, mode='constant', cval=0, clip=True, preserve_range=False)


def saveimg(im, name):
    io.imsave(name, im)

def isgray(im):
    if (len(im.shape) == 2):
        return True
    else:
       return False


# im = imread("test.png")
# gray = grayscale(im)
# cond = isgray(gray)
"""print(""+str(im.shape))
gray = grayscale(im)
print(""+str(gray.shape))
plti(gray)
plti(im)"""
