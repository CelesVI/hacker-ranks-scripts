import numpy as np
from sys import stdin
n,m = map(int, input().split())
for i in range(n):
    arr = np.array([list(map(int, stdin.readline().split()))])
print(np.max(np.min(arr, axis=1)), axis=0)
