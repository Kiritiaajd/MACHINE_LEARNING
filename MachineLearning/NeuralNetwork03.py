import numpy as np

inputs = [1, 2, 3, 4, 5, 6]
weights = [[0.1, 2.1, -3.9, 4.8, -9.0, 0.6],
           [0.1, 1.1, -3.9, 3.8, -3.0, 7.6],
           [0.1, 9.1, -3.9, 6.8, 4.5, 3.6]]

biases = [2.8, 3.1, 4.9, 2.4]

output = np.dot(inputs, weights) + biases
