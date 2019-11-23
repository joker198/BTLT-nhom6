import numpy as np

def linearConvolve(inSignal, impulseResponse):
    h = len(inSignal)+len(impulseResponse) - 1
    w = len(inSignal)
    linearMatrix = np.zeros((h, w))
    des = 0
    src = 0
    linearMatrix[0][0] = impulseResponse[0]
    for y in np.arange(1,h):
        src = y
        if y >= len(impulseResponse):
            if y <= len(inSignal)-1:
                des = y - len(impulseResponse)+1
                pass
            else:
                src = len(inSignal)-1
                des = y-len(impulseResponse)+1
                pass
            pass
        for x in np.arange(src, des-1, -1):
            if w > y:
                linearMatrix[y][x] = impulseResponse[src-x]
                pass
            else:
                linearMatrix[y][x] = impulseResponse[src-x+1+y-w]
                pass
            pass
        pass
    return linearMatrix.dot(inSignal)