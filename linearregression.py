import numpy as np
from builtins import round
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlabel, ylabel
X = np.array([63,64,66,61,69,71,71,72,72,75])
Y = np.array([127,121,142,157,162,156,169,165,181,208])
meanx=np.mean(X)
meany=np.mean(Y)
n=0;
d=0;
for i in range(len(X)):
    n=n+(X[i]-meanx)*(Y[i]-meany)
    d=d+(X[i]-meanx)*(X[i]-meanx)
B1=round(n/d,2);
B0=round(meany-B1*meanx,2)
print("Y=",B1," *  X + ",B0)
plt.scatter(X,Y)
plt.xlabel("Weight")
plt.ylabel("Height")
plt.plot(X,B0+B1*X)
plt.show()