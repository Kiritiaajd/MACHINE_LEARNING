import numpy as np

inputs = [[1, 2, 3, 4],
          [0.2, 0.3, 0.4, 0.5],
          [-0.26, 0.34, -2.1, -0.9]]

weights01 = [[0.1, 2.1, -3.9, 4.8],
             [0.1, 1.1, -3.9, 3.8],
             [0.1, 9.1, -3.9, 6.8]]

biases = [2, 3, 0.5]
biases2 = [-.9, 0.78, -0.88]

weights02 = [[0.1, 0.9, 0.77],
             [0.6, 0.5, 0.3],
             [0.44, 0.55, 0.99]]

layer1_outputs = np.dot(np.array(inputs), np.array(weights01).T) - biases
layer2_outputs = np.dot(layer1_outputs, np.array(weights02).T) - biases2
print(layer1_outputs)
print(layer2_outputs)
