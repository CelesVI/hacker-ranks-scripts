import numpy as np
from sys import stdin
arreglo = np.array(list(map(int, stdin.readline().split())))
print(np.reshape(arreglo,(3,3)))
