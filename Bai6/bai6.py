import numpy as np
import bai601
import bai602
import bai603

inSignal = [0,2,1,9,6,4,6,4,3,6,7,10,3,2,2]
# impulseResponse = [1,1,0,1]
# inSignal = [0,1,2,3,4,5,6,7,8]
impulseResponse = [1,1,0,1]
# inSignal = [1,0,0,1,8,2]
# impulseResponse = [1,0,1]
print("ket qua linear convolution ham co san: ")
print(np.convolve(impulseResponse, inSignal))
print("ket qua linear convolution ham tu lam: ")
print(bai601.linearConvolve(inSignal, impulseResponse))
print("ket qua cyclic convolution ham tu lam: ")
print(bai602.cyclicConvolve(inSignal, impulseResponse))
print("ket qua cyclic convolution ham tu lam theo huong dan trong slide: ")
print(bai603.cyclicConvolution(inSignal, impulseResponse))