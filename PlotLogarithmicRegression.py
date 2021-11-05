
import math
import statistics as stat
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

a = float(fit[0])
b = float(fit[1])

def f(n):
    a*(math.log(n + 1)) + b

def g(n):
    float(math.log(float(L[n]))) - float(math.log(f(n + 1)))

L0 = []
Ln = []
Lp = []
Lpr = []
Ld = []
Lz = []
for n in range(l):
    X = math.log(L[n]) - math.log(a*(math.log(n + 1)) + b)
    
    L0.append(X)
    
    if X < 0:
        Ln.append(X)
    
    else:
        Lp.append(X)
    
    N = len(Ln)
    P = len(Lp)
    Nr = 100*N/(N + P)
    Pr = 100*P/(N + P)
    print("N:P ratio :", round(Nr, 2), ":", round(Pr, 2))
    Lpr.append(Pr)
    
    if n != 0:
        print("StandardDeviation :", stat.stdev(L0))
        Ld.append(stat.stdev(L0))
    
    Z = -math.log10(abs(np.mean(L0)))
    print("MeanSimilarity :", Z)
    Lz.append(Z)

print("\nRegressionLogarithmicCurve :", str(str(a) + "log(x)"), "+", str(b))

plt.plot(L0, 'b_')
plt.show()

plt.hist(L0, bins = 100)
plt.show()

plt.plot(Lpr, 'g-')
plt.show()

plt.plot(Ld, 'r-')
plt.show()

plt.plot(Lz, 'b-')
plt.show()
