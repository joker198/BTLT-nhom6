
import matplotlib.pyplot as plt 
import numpy as np 

f = 1 # tần số cơ bản
fs = 8000  # tần số lấy mẫu
N = 5 # số chu kì tín hiệu 
pi = np.pi # số pi
A = 1 # biên độ
 
t = np.linspace(0, N/f, (N/f) * fs) 

sine = A*np.sin(2*pi*f*t) 
plt.figure()
plt.plot(t,sine) 
plt.xlabel('t')
plt.ylabel('s1(t)')
plt.title('Bai 1.1') 

plt.savefig('bai1-1.png')