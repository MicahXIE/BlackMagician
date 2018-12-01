# encoding UTF-8
def yield_test(n):
	for i in range(n):
		yield call(i)
		print("i=", i)

	print("do something.")
	print("end.")

def call(i):
	return i*2;

for i in yield_test(5):
	print(i, ",")

'''

yield call(0) --> return 0
print("i=", 0)

yield call(1) --> return 2
print("i=", 1)

yield call(2) --> return 4
print("i=", 2)

yield call(3) --> return 6
print("i=", 3)

yield call(4) --> return 8
print("i=", 4)

0 ,
i= 0
2 ,
i= 1
4 ,
i= 2
6 ,
i= 3
8 ,
i= 4
do something.
end.
'''