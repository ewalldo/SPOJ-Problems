#read the number of inputs
n_input = int(input())

for i in range(n_input):
	#read string and get the half position
	value = input()
	half_size_value = len(value) // 2

	#goes through the beggining until the middle of the string jumping every two characters
	output = ""
	for j in range(0, half_size_value, 2):
		output = output + value[j]
		
	#print the output
	print(output)
