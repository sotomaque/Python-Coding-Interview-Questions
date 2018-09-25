
def getClosestPoints(points):
	minDistance = points[0].getDistanceToOrigin()
	minKey = 0
	for i in points:
		distance = points[i].getDistanceToOrigin()
		#print(i, 'distance: ', distance)
		if distance < minDistance:
			minDistance = distance
			minKey = i

	return points[minKey]


def main():

	numPoints = int(raw_input('enter the number of points in set: '))

	# get coordinates for points
	# instanciate point objects
	# iterate and fill hashmap of form { pointID : distanceFromOrigin }
	points = {}
	for i in range(0, numPoints):
		xCoord = int(raw_input('enter the x coordinate: '))
		yCoord = int(raw_input('enter the y coordinate: '))	

		point = Point(xCoord, yCoord)
		points[i] = point

	# get k
	#k = int(raw_input('enter k: '))

	closestPoint = getClosestPoints(points)

	print('the closest point is: ')
	print(closestPoint)
	print(closestPoint.getDistanceToOrigin(), ' units from the origin')


main()