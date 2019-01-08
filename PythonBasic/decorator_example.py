import time

# use to record the func running time
def decorator(func):
	def wrapper(*args, **kwargs):
		t = time.time()
		ans = func(*args, **kwargs)
		t = time.time() - t

		return ans, t

	return wrapper

@decorator
def func():

	for _ in range(10 ** 6):
		x = 0

	return "func"


if __name__ == "__main__":
	print(func())