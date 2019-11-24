import imageio
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft2
from scipy.fftpack import ifft2

im = plt.imread('origin.png')
im_size = im.shape[0] + im.shape[1] + im.shape[2]
fft_im = fft2(im)
imageio.imwrite('real.tif', fft_im.real)
imageio.imwrite('imag.tif', fft_im.imag)

re_im = imageio.imread('real.tif').astype('complex128')
re_im.imag = imageio.imread('imag.tif')
re_im = 255 * (ifft2(re_im).real - np.min(ifft2(re_im).real))
re_im = re_im.astype('uint8')
imageio.imwrite('recover.png', re_im)