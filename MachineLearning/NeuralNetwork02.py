inputs  = [1 ,2,3 ,4 ,5 ,6]
weights = [[0.1 , 2.1 , -3.9 , 4.8 , -9.0, 7.6],
           [0.1 , 1.1 , -3.9 , 3.8 , -3.0, 7.6],
           [0.1 , 9.1 , -3.9 , 6.8 , 4.5, 7.6]]

biases = [2.8,3.1,4.9,2.4]

layer_outputs = []

for neuron_nweights , neuron_biases in zip(weights , biases):
    neuron_output = 0

    for n_input , weight in zip(inputs , neuron_nweights):
        neuron_output+= n_input*weight
    neuron_output += neuron_biases
    layer_outputs.append(neuron_output)

print(layer_outputs)