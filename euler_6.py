import sys
n = sys.stdin.readlines()
del n[0]
for line in n:
    numbers = range(int(line) + 1)
    x = int(line)
    firstsum = (x * (x + 1)) * ((2 * x) + 1)/6
    secondsum = sum(numbers) ** 2
    print (int(secondsum - firstsum))