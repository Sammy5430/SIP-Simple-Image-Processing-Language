import numpy as np
from scipy.signal import convolve2d
from scipy import misc
import matplotlib.pylab as plt
from skimage import feature
from scipy import ndimage
from scipy import misc
from skimage.transform import resize
from skimage.transform import swirl
from skimage.transform import rescale
from skimage import util

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


def canny(im, level):
    intensity = {'HIGH': 1, 'MEDIUM': 3, "LOW": 6}
    edges = feature.canny(im, sigma=intensity[level])
    return edges


def gaussian(im, level, size=13):
    intensity = {'HIGH': (65, 17), 'MEDIUM': (33, 13), 'LOW': (9, 9)}
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

    d = {'right': -90, 'left': 90}
    # Default reshaping is true
    rim = ndimage.rotate(im, d[direction])
    return rim

def translate(im, h, w):

    t_matrix = [[1, 0, 0],
                          [0, 1, 0],
                          [w, h, 1]]
    im = ndimage.interpolation.affine_transform(im, t_matrix,
            offset=0.0, output_shape=None, output=None, order=3, mode='constant', cval=0.0, prefilter=True)

    return im

    # transformed = ndimage.interpolation.affine_transform(im, ((np.cos(0), np.sin(0)), (-np.sin(0), np.cos(0))),
    #                                                 offset=(h, -w), order=3, mode='nearest')


def re_size(im, h, w):
    im = resize(im, (h, w),mode='constant')
    return im

def invert(im):
    return util.invert(im)

def swirly(im):
    return swirl(im, center=None, strength=75, radius=150, rotation=0, output_shape=None, order=1,
                            mode='constant', cval=0, clip=True, preserve_range=False)

def re_scale(im):
    return rescale(im, 2, order=1, mode='constant', cval=0, clip=True, preserve_range=False)


im = imread("a.png")
im2 = re_scale(im)
# im2 = imread("Lenna.jpg")

"""print(""+str(im.shape))
gray = grayscale(im)
print(""+str(gray.shape))
plti(gray)
plti(im)"""
# im = grayscale(im, weights=np.c_[0.2989, 0.5870, 0.1140])
# plt.imshow(im)
plt.imshow(im2)

# sharp = canny(im, 'HIGH')
# plt.imshow(im, cmap='gray')
# plt.imshow(sharp)

# gauss = gaussian(im2, 'HIGH')
# imshow(gauss)
plt.show()