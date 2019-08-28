from collections import defaultdict
from sys import stdin

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    d[input()].append(i+1)
for j in range(m):
    word = input()
    if word == d.key:
        print(d.values[word], sep='\n')
