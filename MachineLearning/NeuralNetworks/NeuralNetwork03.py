import numpy as np

# Correcting the number of biases
inputs = [1, 2, 3, 4, 5, 6]
weights = [[0.1, 2.1, -3.9, 4.8, -9.0, 0.6],
           [0.1, 1.1, -3.9, 3.8, -3.0, 7.6],
           [0.1, 9.1, -3.9, 6.8, 4.5, 3.6]]

# Adjust biases to match the number of output neurons
biases = [2.8, 3.1, 4.9]  # Should match the number of weight rows

# Perform the dot product and add biases
output = np.dot(weights, inputs) + biases

print(output)
