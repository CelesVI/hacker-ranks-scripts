from sys import stdin
from collections import OrderedDict

n = int(input())

dic = OrderedDict()
for _ in range(n):
    item = input().split(' ')
    precio = int(item[-1])
    juntos = " ".join(item[:-1])
    if dic.get(juntos):
        dic[juntos] += precio
    else:
        dic[juntos] = precio
for i,v in dic.items():
    print(i,v)
 
