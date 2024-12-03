import numpy as np

X = [[1, 2, 3, 4],
     [0.2, 0.3, 0.4, 0.5],
     [-0.26, 0.34, -2.1, -0.9]]


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


layer1 = Layer_Dense(4, 5)
layer2 = Layer_Dense(5, 4)

layer1.forward(X)

print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)