''' 
given a sequence of characters, find the longest subsequence within that string 

'''
def longestSubsequence(givenString):
	#key is to go through string only once
	#use a hash map to store longest subsequence
	maxCount = 0
	maxChar = None
	prevChar = None

	for i in range(len(givenString)):
		current = givenString[i]
		if prevChar == current:
			count += 1
		else:
			count = 1
		if count > maxCount:
			maxCount = count
			maxChar = current
		prevChar = current

	return {maxChar: maxCount}



def main():
	print('this program finds the longest subsequence within a given string')
	x = raw_input('please enter a random string with some repeated characters: ')

	print(longestSubsequence(x))

main()