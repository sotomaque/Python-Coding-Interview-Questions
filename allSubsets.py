''' 
problem: write a function that takes an array of n items and prints out all the subsets possible from that given set

input: string

output: character

pattern: 
	number of subsets -> 2^n

'''
debug = True

# helper function called recursively
def helper(givenArray, subset, i):
	if i == len(givenArray):
		print(subset)
	else:
		subset[i] = None
		helper(givenArray, subset, i+1)
		subset[i] = givenArray[i]
		helper(givenArray, subset, i+1)


def allSubsets(givenArray):
	#initialize empty set
	subset = [None] * (len(givenArray))

	helper(givenArray, subset, 0)


def main():
	print('This program prints out all the possible subsets of a given set')
	print('Please enter a string of characters or numbers\n')

	x = raw_input("enter a string: ")
	print('len of input: ', len(x))
	num = int(len(x))
	numOfSubsets = 2**num
	print (x, " has ", numOfSubsets, "subsets")

	allSubsets(x)

main()