import sys

def printStar(num):
    starStrLst = []

    for n in range(1, num+1):
    	starLst = []
    	for i in range(n):
    		starLst.append('*')
    	starStrLst.append(' '.join(starLst))

    for row in range(num):
    	print(' '*(num-1-row)+starStrLst[row])

if __name__ == '__main__':

	inputValue = input()

	try:
		n = int(inputValue)
	except ValueError:
		print("Input value is not a number")
		sys.exit(1)

	printStar(n)
