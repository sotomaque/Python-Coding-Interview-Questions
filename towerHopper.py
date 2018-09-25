''' 
problem: tower hopper

given an array of integers, each integer represents the height of the tower at that index
							
i.e. [4. 2. 0, 0, 2, 0] 

objective: start at index 0, the goal is to try to jump all the way out of the array.
	the maximum amount of step you can jump over depends on the height of the tower you are on

goal: get outside array, not just to the end of the array

'''

def nextStep(currentStep, givenArray):
	# look at starting index, ask whats the next step after that
	# that will allow us to go the furthest in the next step after 


#should return true if tower is hoppable
def isHoppable(givenArray):
	current = 0
	while True:
		if current >= len(givenArray):
			return True
		if givenArray[current] == 0:
			return False
		current = nextStep(current, givenArray)

def main():


main()
