import sys
n = sys.stdin.readlines()
del n[0]
for line in n:
	fn = [0, 1,]
	while fn[-1] < int(line):
		fn.append(fn[-1] + fn[-2])
	del fn[-1]
	print (sum(i for i in fn if i % 2 == 0))