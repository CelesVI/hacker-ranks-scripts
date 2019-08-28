from itertools import combinations
from sys import stdin
c,b = stdin.readline().split()
b = int(b)

for i in c:
    for j in (combinations(sorted(c), b)):
        print (''.join(j), sep='\n')


