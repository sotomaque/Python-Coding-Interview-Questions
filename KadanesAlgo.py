''' 
	Kadanes Algorithm: maximum subarray problem

	find the subarray with the maximum sum
	subarrays must be continuous

'''

def KadanesAlgorithm(givenArray):
	maxCurrent = maxGlobal = givenArray[0]
	for i in range (1, len(givenArray) - 1):
		maxCurrent = max(givenArray[i], maxCurrent + givenArray[i])
		if maxCurrent > maxGlobal:
			maxGlobal = maxCurrent
	print('maximum subarray within ', givenArray, 'is', maxGlobal)
	return


def main():
	print('this program finds the subarray with the maximum sum within a given array of numbers')
	#x = []
	#y = raw_input("enter a string of numbers: ")

	#convert string of numbers into array form
	#for i in y:
	#	x.append(int(i))

	x = [-2, 3, 2, -1]

	KadanesAlgorithm(x)

main()