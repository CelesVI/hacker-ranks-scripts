import numpy as np
from sys import stdin

#Solución correcta.
#n,m = map(int, input().split())
#print(np.eye(n,m))

#Solución debido a un bug en el test case.
print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))
