inputs  = [1 ,2,3 ,4 ,5 ,6]
weights = [0.1 , 2.1 , -3.9 , 4.8 , -9.0, 7.6]
bias = 0.5
output = 0
for  i in range(len(inputs)):
    output = inputs[i] * weights[i] + bias


print(output)
actual_output = [2 , 3, 4,6,1,7]


