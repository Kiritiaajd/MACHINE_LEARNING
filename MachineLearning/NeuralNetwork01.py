inputs  = [1 ,2,3 ,4 ,5 ,6]
weights1 = [0.1 , 2.1 , -3.9 , 4.8 , -9.0, 7.6]
weights2 = [0.1 , 1.1 , -3.9 , 3.8 , -3.0, 7.6]
weights3 = [0.1 , 9.1 , -3.9 , 6.8 , 4.5, 7.6]
bias1 = 0.5
bias2 = 0.9
bias3 = 0.7
output = 0
for  i in range(len(inputs)):
    output11 = inputs[i] * weights1[i] + bias1
    output12 = inputs[i] * weights2[i]  + bias2
    output13 = inputs[i] * weights3[i]   + bias3




print(output11)
print(output12)
print(output13)
# Now we are going to calculate the final neuron 
weights21 = [1.2 , 3,4.5 , 9, 5.4 , 6.6]
bias21 = 0.9

final_neuron =   0

for i  in range(len(weights21)):
    final_neuron = output11 * weights21[i]+ output12 * weights21[i] + bias21


print(final_neuron)
target = 550

error =  target - final_neuron

#  Now we are going to calculate the error gradient of the final neuron




