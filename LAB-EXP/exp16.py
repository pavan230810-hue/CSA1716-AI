import numpy as np

x = np.array([[1, 2]])
w1 = np.array([[0.5, 0.2],
               [0.3, 0.4]])

w2 = np.array([[0.6], [0.7]])

hidden = np.maximum(0, np.dot(x, w1))
output = 1 / (1 + np.exp(-np.dot(hidden, w2)))

print("Output:", output)
