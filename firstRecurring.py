''' 
problem: 
 given a string of N characters, return the first recurring character in a string

 input: string

 output: character

 solution 1:
 	first look at character @ index 0
 	see if you can find it in subsequent string 
 	i.e. Given "DBCABA" look for 'D' in "BCABA"
 run complexity: N choose(2) -> (n)(n-1)/2 -> O(n^2)

 better solution:
 	use a data structure such as a dictionary or a hash map to store characters and their counts
 	return first non single count
'''

def firstRecurring(givenString):
	counts = {}
	for char in givenString:
		if char in counts:
			print('Recurrance Found! First Recurring Character: ')
			return char
		else:
			counts[char] = 1
	print('No Recurrance in given string!')
	return None

# run complexity O(n)



def main():
	print('First Recurring Character in a String\n')

	x = raw_input("enter a string: ")
	print(x)

	print(firstRecurring(x))

main()