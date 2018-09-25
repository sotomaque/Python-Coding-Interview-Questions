''' 
if you have two sorted arrays, find the common elements of the arrays

'''

def intersection(givenArray1, givenArray2):
	common = []
	x = y = maxLength = 0
	if (len(givenArray1) >= len(givenArray2)):
		maxLength = len(givenArray1)
	else:
		maxLength = len(givenArray2)

	for i in range(maxLength):
		print('x', x)
		print('y', y)
		if (givenArray1[x] == givenArray2[y]):
			common.append(givenArray1[x])
			x += 1
			y += 1
		elif (givenArray1[x] < givenArray2[y]):
			x += 1
		else:
			y += 1

	if len(common) == 0:
		print('no common elements found')
		return
	else:
		print(len(common), ' common elements found')
		return common


def bubbleSort(list):
	# Swap the elements to arrange in order
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp

def main():
	#description
	print("This program takes in a series of arrays and returns the common elements between them")
	
	#input
	array1 = raw_input("enter the first array: ")
	array2 = raw_input("enter the second array: ")
	x = []
	y = []

	#put stirngs into array form
	for i in array1:
		x.append(int(i))
	for i in array2:
		y.append(int(i))

	#sort arrays
	bubbleSort(x)
	bubbleSort(y)

	print('x: ', x)
	print('y: ', y)

	#return common elements 
	print(intersection(x, y))


main()