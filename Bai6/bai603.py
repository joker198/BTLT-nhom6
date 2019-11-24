import numpy as np

def cyclicConvolution(x, h):
    h1 = np.zeros(len(x))
    for i in np.arange(0, len(x)):
        if i < len(h):
            h1[i] = h[i]
    h2 = np.array(h1)
    h2 = np.append(h2, h1)
    return np.convolve(x, h2)[len(x):len(x)*2]