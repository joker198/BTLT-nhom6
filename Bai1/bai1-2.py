 
import matplotlib.pyplot as plt 
import numpy as np 
  
f = 1 # tần số cơ bản
fs = 2000 # tần số lấy mẫu
pi = np.pi # số pi
N = 5 # số chu kì tín hiệu 
A = 2 # biên độ
t = np.linspace(0, N/f, (N/f) * fs)
sine = np.zeros(len(t))
n = 10

for i in np.arange(0, 2*n+2):
	m = 2*i +1
	sine += (A/(m*m))*np.sin(2*m*pi*f*t)
	
plt.plot(t,sine) 	
plt.xlabel('t')
plt.ylabel('s2(t)')
plt.title('Bai 1.2') 	
plt.savefig('bai1-2.png')