import numpy as np

# inSignal = [1,0,0,1,8,2]
# impulseResponse = [1,1,0,1]

def cyclicConvolve(inSignal, impulseResponse):
    size = len(inSignal)
    cylicMatrix = np.zeros((size, size))
    for y in np.arange(0, size):
        if y < len(impulseResponse)-1:
            for x in np.arange(y, -1, -1):
                cylicMatrix[y][x] = impulseResponse[y-x]
                pass
            for x in np.arange(size+y-len(impulseResponse)+1, size):
                cylicMatrix[y][x] = impulseResponse[size-x+y]
                pass
            pass
        else:
            for x in np.arange(y, y-len(impulseResponse), -1):
                cylicMatrix[y][x] = impulseResponse[y-x]
                pass
            pass
        pass
    return cylicMatrix.dot(inSignal)