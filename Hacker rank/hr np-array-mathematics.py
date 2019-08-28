import numpy as np
from sys import stdin
n,m = input().split()
a = np.array([list(map(int, stdin.readline().split()))])
b = np.array([list(map(int, stdin.readline().split()))])
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')
