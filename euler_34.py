import sys
import math

def evaluate(num):
	sum = 0
	array = ([int(i) for i in str(num)])
	for number in array:
		sum += math.factorial(number)
	return sum%num == 0
		
	
	
def numberLister(input):
	sum = 0
	for num in range(10,input):
		if evaluate(num):
			sum += num
	return sum

x = int(sys.stdin.readline())
print(numberLister(x))