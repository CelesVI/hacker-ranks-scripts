import numpy as np
from sys import stdin

#n, m, o = (map(int, input().split()))
#for i in range(o):
 #   print(np.zeros((n,m), dtype=np.int))
 #   print('\n')
#for j in range(o):
 #   print(np.ones((n,m), dtype=np.int))
 #   print('\n')
forma = tuple(map(int, input().split()))
print (np.zeros(forma, dtype = np.int))
print (np.ones(forma, dtype = np.int))
