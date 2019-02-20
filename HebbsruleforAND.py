x1 = [1, 1, -1, -1]
x2 = [1, -1, 1, -1]
y = [1, -1, -1, -1]
b = 0
w1 = 0
w2 = 0
f = []
for i in range(0, 4):
    f.append(b + x1[i] * w1 + x2[i] * w2)

while f != y:
    for i in range(0, 4):
        while f[i] != y[i]:
            w1 = w1 + x1[i] * y[i]
            w2 = w2 + x2[i] * y[i]
            b = b + y[i]
            f[i] = b + x1[i] * w1 + x2[i] * w2
            if f[i] >= 1:
                f[i] = 1
            else:
                f[i] = -1
print(w1)
print(w2)
print(b)
print(f)
