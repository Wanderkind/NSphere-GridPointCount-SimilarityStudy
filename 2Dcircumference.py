
import matplotlib.pyplot as plt
import math

M = int(input('MaxR : '))

L = []
for R in range(M):
    r = R + 1

    a = math.ceil(math.sqrt(2)*r) + 1
    
    Count = 1
    for I in range(r):
        i = I + 1
        
        for J in range(min(r, a - i) - R + i + 1):
            j = J + 1 + r - i
            
            if r - 0.5 < math.sqrt(i**2 + j**2) < r + 0.5:
                Count = Count + 1

    CIR = 4*Count/(2*math.pi*r)
    Index = -round(math.log10(abs(math.log(CIR))), 4)
    print(r, ';', Index)
    L.append(Index)

plt.plot(L, 'b_')
plt.show()
