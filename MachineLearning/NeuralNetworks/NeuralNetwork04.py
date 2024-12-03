import numpy as np

# Reshape inputs to have 6 rows and 3 columns
inputs = [[1, 0.2, -0.26],
          [2, 0.3, 0.34],
          [3, 0.4, -2.1],
          [4, 0.5, -0.9],
          [5, 0.6, 0.1],
          [6, 0.7, 0.99]]


# Adjust weights to have shape (3, 3) for dot product with (6, 3)
weights02 = [[0.1, 2.1, -3.9],
             [0.1, 1.1, 9.1],
             [0.1, -3.9, 6.8]]

# Adjust biases to match the output shape (3,)
biases = [2, 3, 0.9]

# Convert to NumPy arrays
inputs_array = np.array(inputs)  # Shape (6, 3)
weights_array = np.array(weights02)  # Shape (3, 3)

# Perform the dot product
output = np.dot(inputs_array, weights_array) + biases

print(output)



