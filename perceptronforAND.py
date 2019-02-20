import matplotlib.pyplot as plt
import numpy as np
x1 = [1, 1, -1, -1]
x2 = [1, -1, 1, -1]
y = [1, -1, -1, -1]

b = 0
w1 = 0
w2 = 0
alpha=0.25
threshold=0
f = []
for i in range(0, 4):
    f.append(b + x1[i] * w1 + x2[i] * w2)

while f != y:
    for i in range(0, 4):
        while f[i] != y[i]:
            w1 = w1 + x1[i] * y[i]*alpha
            w2 = w2 + x2[i] * y[i]*alpha
            b = b + y[i]*alpha
            f[i] = b + x1[i] * w1 + x2[i] * w2
            if f[i] >= threshold:
                f[i] = 1
            else:
                f[i] = -1
print("w1=",w1)
print("w2=",w2)
print("b=",b)
print("f=",f)
x1=np.array(x1)
Y=(-b-w1*x1)/w2
plt.plot(x1,Y)
plt.plot(x1*2,[0]*4)
plt.plot([0]*4,x1*2)
plt.show()