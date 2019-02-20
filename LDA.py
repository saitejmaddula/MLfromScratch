import pandas as pd
import numpy as np
import math

data=pd.read_csv("C:/Users/saitej/Desktop/data/mydata.csv",header=None)

X1=data[[0,1]][:4]
Y1=data[2][:4]
X2=data[[0,1]][4:7]
Y2=data[2][4:7]
Xmean=data.groupby([2]).mean()

X1mean=Xmean[[0,1]][:1]
X2mean=Xmean[[0,1]][1:2]

X1mean=X1mean.values
X2mean=X2mean.values
Xmean=np.array([2.88,5.67])

X1=X1.values
X2=X2.values
correctedX1=X1-Xmean
correctedX2=X2-Xmean

C1=np.dot(np.transpose(correctedX1),correctedX1)/4
C2=np.dot(np.transpose(correctedX2),correctedX2)/3

C=(4/7)*C1+(3/7)*C2

invC=np.linalg.inv(C)
print(invC)
test=np.array([2.18,5.24])

f1=np.dot(np.dot(X2mean,invC),np.transpose(test))-0.5*np.dot(np.dot(X2mean,invC),np.transpose(X2mean))+math.log(4/7)
f2=np.dot(np.dot(X1mean,invC),np.transpose(test))-0.5*np.dot(np.dot(X1mean,invC),np.transpose(X1mean))+math.log(3/7)
if f1>f2:
    print("Not Passed")
else:
    print("passed")    