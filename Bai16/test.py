import numpy as np

# a = np.zeros((3,4)) #=> Ma trận 0
# a = np.ones((3,4)) #=> Ma trận 1
# a = np.arange(0,10,1.5)
# a = np.linspace(0,10,6) # => Tạo một đường thẳng, và chia đoạn cách đều
# a = np.eye(3)
a = np.arange(12)
print(a)
b = a.reshape(3,4)
print(b) 
print(b.flatten())

