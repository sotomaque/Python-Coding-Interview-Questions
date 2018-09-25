''' 
problem: 
 given a -> 1
 	   b -> 2
 	   ...
 write a function that takes a string of numbers as an input and returns the number of messages that could have been the original message
 aka how many ways are there to decode this original message

 i.e. given data = '12' :: numWaysToDecode(12) should return 2 
 		(1) -> 'a', 'b'
 		(2) -> 'l'

 		i.e. numWaysToDecode(12) -> return sizeOf( {[a,b], l} )

 input: string of numbers
 output: int count of potential original messages

 examples:

 N     ||	numWaysToDecode(N)
 ------------------------------
 ''	   ->	numWaysToDecode('') -> 1
 3	   ->	numWaysToDecode(3)  -> 1
 12345 ->	numWaysToDecode(12345) -> {a + numWaysToDecode(2345)} or {l + numWaysToDecode(345)}
 27345 ->	numWaysToDecode(27345) -> {b + numWaysToDecode(7345)} 
 011   ->	0

'''
# helper takes in data and a non-negative #, k
# helper only looks at last k characters of data
# this way we dont have to create a new string every time we call our function recursively
# will return the number of ways we can decode the last k letters of a string
def helper(data, k):
	#base cases:
	# 1: when string is empty
	print('k: ', k)
	if k == 0: return 1
	# 2: when the given string starts with a 0

	# define new var which will be the starting index i.e. give {"12345", 3} s -> 2
	s = len(data) - k
	print('s: ', s)
	if data[s] == '0': return 0

	# with recursive case, sometimes we have to call recursion twice (i.e. when two digit mapping <= 26)
	# sometimes we only have to call it once (i.e. when two digit mapping > 26)
	result = helper(data, k-1)
	if k >= 2 and int(data[s:s+2]) <= 26:
		result += helper(data, k-2)
	
	return result

def numWaysToDecode(data):
	print('data: ', data)
	print('length of data: ', len(data))
	return (helper(data, len(data)))

def main():
	print('how many ways are there to decode this original message\n')

	x = raw_input("enter a string: ")
	#print(x)

	print(numWaysToDecode(x))

main()