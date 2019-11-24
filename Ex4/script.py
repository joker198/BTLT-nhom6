import imageio
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft2
from scipy.fftpack import ifft2

def scale(X, x_min, x_max):
    nom = (X-X.min(axis=0))*(x_max-x_min)
    denom = X.max(axis=0) - X.min(axis=0)
    denom[denom==0] = 1
    return x_min + nom/denom 


im = plt.imread('origin.png')

rf_im = fft2(im).real
rf_min = np.min(rf_im)
rf_im[:,:,0] = scale(rf_im[:,:,0], 0, 255)
rf_im[:,:,1] = scale(rf_im[:,:,1], 0, 255)
rf_im[:,:,2] = scale(rf_im[:,:,2], 0, 255)
try:
    rf_im[:,:,3] = scale(rf_im[:,:,3], 0, 255)
except:
    print("FFT: image don't has alpha field")
rf_im = rf_im.astype('uint8')
imageio.imwrite('real.png', rf_im)

if_im = fft2(im).imag
if_im[:,:,0] = scale(if_im[:,:,0], 0, 255)
if_im[:,:,1] = scale(if_im[:,:,1], 0, 255)
if_im[:,:,2] = scale(if_im[:,:,2], 0, 255)
try:
    if_im[:,:,3] = scale(if_im[:,:,3], 0, 255)
except:
    print("FFT: image don't has alpha field")
if_im = if_im.astype('uint8')
imageio.imwrite('imag.png', if_im)

re_im = plt.imread('real.png').astype('complex128')
re_im.imag = plt.imread('imag.png')
re_im = ifft2(re_im).real
re_im[:,:,0] = scale(re_im[:,:,0], 0, 255)
re_im[:,:,1] = scale(re_im[:,:,1], 0, 255)
re_im[:,:,2] = scale(re_im[:,:,2], 0, 255)
try:
    re_im[:,:,3] = scale(re_im[:,:,3], 0, 255)
except:
    print("IFFT: image don't has alpha field")
re_im = re_im.astype('uint8')
imageio.imwrite('recover.png', re_im)

test = fft2(im).real.astype('complex128')
test.imag = fft2(im).imag
test = 255 * ifft2(test).real
test = test.astype('uint8')
imageio.imwrite('test.png', test)