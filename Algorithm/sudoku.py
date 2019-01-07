# https://www.jianshu.com/p/d920ff682623
# https://blog.csdn.net/littlethunder/article/details/9749509
# https://www.jb51.net/article/110940.htm
# https://blog.csdn.net/littlethunder/article/details/9749509

import time

class point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.available = []
		self.value = 0

#pointLst = []

def checkAvailableValue(value, pointObj, sudokuLst):
	if value in sudokuLst[pointObj.x]:
		return False

	for row in range(0,9):
		if value == sudokuLst[row][pointObj.y]:
			return False

	blockRow, blockCol = pointObj.x//3*3, pointObj.y//3*3

	block = sudokuLst[blockRow][blockCol:blockCol+3] + sudokuLst[blockRow+1][blockCol:blockCol+3] + sudokuLst[blockRow+2][blockCol:blockCol+3]

	for block_item in block:
		if block_item == value:
			return False

	return True

def checkPointValue(pointObj, sudokuLst):
	if pointObj.value == 0:
		print("not assign value to point: ", pointObj.x, pointObj.y)
		return False
	
	if checkAvailableValue(pointObj.value, pointObj, sudokuLst):
		return True
	else:
		return False

def initPoint(sudokuLst):
	pointLst = []

	for x_value in range(9):
		for y_value in range(9):
			if sudokuLst[x_value][y_value] == 0:
				pointObj = point(x_value, y_value)

				for value in range(1, 10):
					if checkAvailableValue(value, pointObj, sudokuLst):
						pointObj.available.append(value)

				pointLst.append(pointObj)

	return pointLst

def tryInsert(pointObj, sudokuLst):

	for value in pointObj.available:
		pointObj.value = value

		#print("x: %d, y: %d  value: %d" % (pointObj.x, pointObj.y, pointObj.value))

		if checkPointValue(pointObj, sudokuLst):
			sudokuLst[pointObj.x][pointObj.y] = pointObj.value

			if len(pointLst) <= 0:
				printSudoku(sudokuLst)
				exit()
			else:
				pointObjNext = pointLst.pop()
				tryInsert(pointObjNext, sudokuLst)
				sudokuLst[pointObjNext.x][pointObjNext.y] = 0
				sudokuLst[pointObj.x][pointObj.y] = 0
				pointObjNext.value = 0
				pointLst.append(pointObjNext)
		else:
			pass


def printSudoku(sudokuLst):

	for x_value in range(9):
		for y_value in range(9):
			print(sudokuLst[x_value][y_value], end=" ")
		print("")


if __name__ == '__main__':

	sudokuLst = [
	[8,0,0,0,0,0,0,0,0],
	[0,0,3,6,0,0,0,0,0],
	[0,7,0,0,9,0,2,0,0],
	[0,5,0,0,0,7,0,0,0],
	[0,0,0,8,4,5,7,0,0],
	[0,0,0,1,0,0,0,3,0],
	[0,0,1,0,0,0,0,6,8],
	[0,0,8,5,0,0,0,1,0],
	[0,9,0,0,0,0,4,0,0]]

	pointLst = initPoint(sudokuLst)
	printSudoku(sudokuLst)
	print("")
 	
	pointObj = pointLst.pop()
	tryInsert(pointObj, sudokuLst)










