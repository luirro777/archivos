import numpy as np
a = np.array([[1, 1],[2,4]])
print(a)
b = np.array([35, 94])
print(b)
c = np.linalg.inv(a).dot(b)
print(c)


