''' 
problem: given an array, find and return the second largest number in the array

'''

def secondLargest(givenArray):
	'''ideas: 
			1) sort array, delete largest element, return new max
	'''
	if len(givenArray) == 0 or len(givenArray) == 1: return

	n = [None] * (len(givenArray) - 1)
	
	for i in range(len(givenArray)):
		temp = givenArray[i]

		if (max(givenArray) == temp): 
			i+=1
		else:
			n[i] = temp

	return max(n)


def main():
	print("This program takes in an array and returns the second largest number in that array")
	x = raw_input("enter a string of numbers: ")
	y = []

	for i in x:
		y.append(int(i))


	print(secondLargest(y))

main()



