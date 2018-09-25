''' 
problem: randomly reorder an array in O(n) time

'''

import math
from random import randint

def reorder(givenArray):
	n = len(givenArray)
	for i in range(n-1, 1, -1):
		pick = math.floor((i+1) * randint(0, 1))
		#print('pick:', pick)
		temp = givenArray[i]
		#print('temp:', temp)
		givenArray[i] = givenArray[int(pick)]
		#print('givenArray[i]:', givenArray[i])
		#print('givenArray[int(pick)]:', givenArray[int(pick)])
		givenArray[int(pick)] = temp
		#print('givenArray[int(pick)]:', givenArray[int(pick)])


def main():
	print('This program randomly reorders elements of an array in O(n) time')

	x = []
	y = raw_input("enter a string of numbers: ")

	#convert string of numbers into array form
	for i in y:
		x.append(int(i))

	print('You entered:', x)

	reorder(x)

	print('After being shuffled:', x)


main()