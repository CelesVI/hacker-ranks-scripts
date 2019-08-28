import numpy as np
from sys import stdin
n, m = map(int,input().split())
arreglo = np.array([list(map(int, stdin.readline().split())) for i in range(n)], int)
#for i in range(n):
 #   arregloBis = np.array([])
 #   arregloBis = np.array(list(map(int, stdin.readline().split())))
 #   arreglo = np.append(arreglo, arregloBis)
print(arreglo.transpose())
print(arreglo.flatten())
