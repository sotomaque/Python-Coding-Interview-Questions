''' 
problem: 
 write a function that returns the number of ways you can go from the bottom of a stair case to the top
 given you are allowed to take single and double steps

 input: int, N

 output: int, numWays

 edge cases: 

 	N = 0 :: numWays -> 1
 	N = 1 :: numWays -> 1
 	N = 2 :: numWays -> 2
 	N = 3 :: numWays -> 3
 	N = 4 :: numWays -> 5

 pattern: fib!
 	in N = 4, after first step solution is identical to N = 3


 solution 1:
 	use fib algorithm 
 	i.e. numWays(3) = numWays(2) + numWays(1)

 run complexity: 

 better solution:
 	dp bottom up approach
'''

debug = False 

def numWays(n):
	#edge cases
	if n == 0 or n == 1:
		return 1
	else:
		return numWays(n-1) + numWays(n-2)

'''
i.e. 
	say we want numWays(4) -> start with 0,1, add up two previous to get numWays(2) = 1, continue until numWays 4

	need an array size n + 1

'''
def numWaysDP(n):
	if n == 0 or n == 1: return 1
	nums = [None] * (n+1)
	if (debug): print(nums)
	nums[0] = 1
	nums[1] = 1

	for i in range(2, n+1):
		if (debug): print(i)
		nums[i] = nums[i-1] + nums[i-2]
		if (debug): print(nums)

	return nums[n]



def main():
	#description
	print('Recursive Staircase Problem\n')

	#input
	x = int(raw_input("enter the number of steps in a given staricase: "))
	print(numWays(x))

	# Dynamic Programming Alternative

	#description
	print('Same Problem Done With Dynamic Programming\n')

	#input
	y = int(raw_input("enter the number of steps in a given staricase: "))
	print(numWaysDP(y))



main()