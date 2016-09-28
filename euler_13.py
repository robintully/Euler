import sys
n = sys.stdin.readlines()
del n[0]
x = 0
for line in n:
    x += int(line)
x = str(x)
print (x[:10])