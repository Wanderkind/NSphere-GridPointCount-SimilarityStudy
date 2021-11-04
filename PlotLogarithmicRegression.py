
import math
import numpy as np
import matplotlib.pyplot as plt

L = []

while True:
    X = input()
    
    if X != '':
        L.append(float(X))
        
    else:
        break

l = len(L)

x = np.arange(1, l + 1, 1)
y = np.array(L)

fit = np.polyfit(np.log(x), y, 1)
print(fit)

a = float(fit[0])
b = float(fit[1])

def f(n):
    a*(math.log(n + 1)) + b

def g(n):
    float(math.log(float(L[n]))) - float(math.log(f(n + 1)))

L0 = []
Ln = []
Lp = []
Lz = []
for n in range(l):
    X = L[n] - (a*(math.log(n + 1)) + b)
    
    L0.append(X)
    
    if X < 0:
        Ln.append(X)
    
    else:
        Lp.append(X)
    
# plt.plot(L0, 'b_')
# plt.show()
    
    N = len(Ln)
    P = len(Lp)

    print(round(100*N/(N + P), 2), ":", round(100*P/(N + P), 2))
    
    Z = -math.log(abs(np.mean(L0)))
    print(Z)
    Lz.append(Z)

plt.hist(L0, bins = 80)
plt.show()

plt.plot(Lz, 'b_')
plt.show()
