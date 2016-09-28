def calc(n):
	newnum = str(2 ** n)
	total = 0
	for x in newnum:
		total += int(x)
	print(total)

import sys
inputs = sys.stdin.readlines()
del inputs[0]
for line in inputs:
    calc(int(line))