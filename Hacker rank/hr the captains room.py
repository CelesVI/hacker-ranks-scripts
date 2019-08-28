from collections import Counter
from sys import stdin
#Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs

a = int(input())
hab = list(map(int, stdin.readline().split()))
dic = Counter(hab)
#for key, value in dic.items():
#    if dic.get(key) == 1:
#        b = dic.get(key)
#print(b)
print(dic)
