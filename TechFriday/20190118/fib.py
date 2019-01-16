import sys

def fibonacci(num):

	if num == 1:
		return 0

	if num == 2:
		return 1


	res = fibonacci(num-1) + fibonacci(num-2)

	return res


if __name__ == '__main__':

	inputValue = input()

	try:
		n = int(inputValue)
	except ValueError:
		print("Input value is not a number")
		sys.exit(1)

	res = fibonacci(n)

	print(res)