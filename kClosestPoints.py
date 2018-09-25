''' 
problem: K closes points to the origin
input: array of tuples
output: n element array, printing out tuples of cloeset points to origin

'''
import math

def getPoints():
	x = []
	y = raw_input("Enter an even # of numbers: ")
	if len(y) % 2 != 0:
		print("Invalid input")
		return 

	for i in y:
		x.append(int(i))
	print(x)
	return x


def pythagreanDistance(givenArray):
	if len(givenArray) != 2: 
		return
	else: 
		xPoint = float(givenArray[0])
		yPoint = float(givenArray[1])
		distance = float(math.sqrt(xPoint**2 + yPoint**2))

		return distance



def kClosestPoints(k):
	#temp hardcode tuples
	temp = [[0, -2], [-2, 4], [-1, 0], [3, 5], [3, 2], [-2, -3], [0, 1]]

	#initialize empty array of distances 
	x = []

	#iterate and find each tuples distance from origin
	#storing the values in x
	for i in range(len(temp)):
		point = temp[i]
		dist = pythagreanDistance(point)
		x.append(float(dist))

	print("\n")
	if int(k) == 1:
		num = x.index(min(x))
		print('closest point to origin is :' , temp[num],  min(x), 'units from the center')
		print("\n")
	else:
		z = []
		for i in range(len(x)):
			z.append(x[i])
		print('z: ', z)
		y = []
		for i in range(k):
			shortestDistanceIndex = x.index(min(z))
			closestPoint = temp[shortestDistanceIndex]
			y.append(closestPoint)
			print(y)
			del z[shortestDistanceIndex]
			print('z: ', z)
			print('x:', x)

		print('closest points:', y)




def main():
	#describe
	print('this function prints out the K cloest points to the origin')

	#input points
	#points = []
	#points = getPoints()

	#convert raw points into tuple data structure

	
	#input K
	k = int(raw_input('Enter K: '))
	kClosestPoints(k)


main()