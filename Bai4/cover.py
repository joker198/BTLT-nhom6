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