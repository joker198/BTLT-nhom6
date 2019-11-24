import imageio
import numpy as np
import matplotlib.pyplot as plt

def rgba2gray(rgba_im):
    r, g, b = rgba_im[:,:,0], rgba_im[:,:,1], rgba_im[:,:,2]
    gray = rgba_im.copy()
    gray[:,:,0] = 0.3 * r + 0.59 * g + 0.11 * b
    gray[:,:,1] = 0.3 * r + 0.59 * g + 0.11 * b
    gray[:,:,2] = 0.3 * r + 0.59 * g + 0.11 * b
    try:
        gray[:,:,3] = 1
    except:
        print("Gray: image don't has alpha field")
    return 255 * gray

def rgba2red(rgba_im):
    red = rgba_im.copy()
    red[:,:,1] = 0
    red[:,:,2] = 0
    try:
        red[:,:,3] = 1
    except:
        print("Red: image don't has alpha field")
    return 255 * red
    
def rgba2green(rgba_im):
    green = rgba_im.copy()
    green[:,:,0] = 0
    green[:,:,2] = 0
    try:
        green[:,:,3] = 1
    except:
        print("Green: image don't has alpha field")
    return 255 * green
    
def rgba2blue(rgba_im):
    blue = rgba_im.copy()
    blue[:,:,0] = 0
    blue[:,:,1] = 0  
    try:
        blue[:,:,3] = 1
    except:
        print("Blue: image don't has alpha field")
    return 255 * blue
    
def rgba2alpha(rgba_im):
    alpha = rgba_im.copy()
    alpha[:,:,0] = 0
    alpha[:,:,1] = 0
    alpha[:,:,2] = 0
    return 255 * alpha
    
def recover(rscale_im, gscale_im, bscale_im, ascale_im):
    rgba = rscale_im.copy()
    rgba[:,:,1] = gscale_im[:,:,1]
    rgba[:,:,2] = bscale_im[:,:,2]
    try:
        rgba[:,:,3] = ascale_im[:,:,3]
    except:
        print("Recover: image don't has alpha field")
    return 255 * rgba

rgba_im = plt.imread('origin.png')

gray_im = rgba2gray(rgba_im).astype('uint8')
imageio.imwrite('gray.png', gray_im)

red_im = rgba2red(rgba_im).astype('uint8')
imageio.imwrite('red.png', red_im)

green_im = rgba2green(rgba_im).astype('uint8')
imageio.imwrite('green.png', green_im)

blue_im = rgba2blue(rgba_im).astype('uint8')
imageio.imwrite('blue.png', blue_im)

alpha_im = rgba2alpha(rgba_im).astype('uint8')
imageio.imwrite('alpha.png', alpha_im)

rscale_im = plt.imread('red.png')
gscale_im = plt.imread('green.png')
bscale_im = plt.imread('blue.png')
ascale_im = plt.imread('alpha.png')
rergba_im = recover(rscale_im, gscale_im, bscale_im, ascale_im).astype('uint8')
imageio.imwrite('recover.png', rergba_im)
