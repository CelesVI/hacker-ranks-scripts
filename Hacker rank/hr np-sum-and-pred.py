import numpy as np
from sys import stdin
n,m = map(int, input().split())
arr = np.array([])
for i in range(n): 
    #a = np.array([list(map(int, stdin.readline().split()))])
    arr = np.append(arr, np.array([list(map(int, stdin.readline().split()))]), axis=0)
print(np.prod(np.sum(arr, axis=0)))
