'''
problem: given an array of numbers, which when combined (concatinated) make a whole number,
		 add one to the number

i.e. [1,2,3,4] represents 1,234;
						 +    1
						 ------
				return	  1,235 but in array from [1,2,3,5]


pre-coding process: 
	-could this array be empty?
	-can we always assume that each element of this array is always an int between 0 - 9
	-different approaches: 1) iterative 2) recursive


'''

def addOne(givenArray):
	#edge case: when given array is of form [9,9,9,..] new array will have to be of 
	#	len(givenArray) + 1
	#	otherwise, new array will be of size len(givenArray)
	carry = 1
	result = [None] * len(givenArray)
	#print(result)
	#print("length: ", len(givenArray))
	for i in range(len(givenArray) - 1, 0, -1):
		total = givenArray[i] + carry
	
		if total == 10:
			carry = 1
		else:
			carry = 0

		result[i] = total % 10

	if carry == 1:
		result = [None] * (len(givenArray) + 1)
		result[0] = 1

	return result

def main():
	print('This program adds one to a number given in parsed array form')
	print('Please enter a number\n')
	x = []
	y = raw_input("enter a string of numbers: ")

	#convert string of numbers into array form
	for i in y:
		x.append(int(i))

	#print(x)

	#pass array form to function
	print(addOne(x))

main()