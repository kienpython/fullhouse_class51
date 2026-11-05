import numpy as np
a = np.arange(1, 26).reshape(5, 5)
# print(a)
# print(a[1,2])
# print(a[-1,:])
# print(a[:,0])
# print(a[1:4,1:4])
# print(a[::2,:])
# print(a[a%3==0])
# print(np.where(a>20))
# print(a[:2,-2:])
# b = a.copy()
# b[b%2==0]=0
# print(b)

# p = a[:2]
# q = a[3:]
# print("===============")
# print(p)
# print("===============")
# print(q)
# print("==================")
# print(np.vstack((p,q)))
# print("==================")
# print(np.hstack((p,q)))

M = np.arange(12).reshape(3, 4)
print(M)
v = np.array([100, 200, 300, 400])
w = np.array([1, 2, 3])
print(M+v)
