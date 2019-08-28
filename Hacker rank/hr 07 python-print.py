import sys
n = int(input())
a = []
i = 0
for i in range(n):
    a.append(i+1)
    
print (*a, sep='')
#sys.stdout.flush()
