#read how many input
n_input = int(input())

for i in range(n_input):
	#read line and separate the values
	value_1, value_2 = input().split(' ')

	#invert the strings and convert to int
	value_1 = int(value_1[::-1])
	value_2 = int(value_2[::-1])

	#calculate the sum and invert the result
	output = str(value_1 + value_2)[::-1]

	#print the output
	print(int(output))
