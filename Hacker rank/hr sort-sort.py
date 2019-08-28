from sys import stdin
from operator import itemgetter
n, m = map(int, input().split())
#atletas = []
#for i in range(n):
temp = [[list(map(int, stdin.readline().split()))] for i in range(n)]
    #atletas.append(temp)
for j in sorted(temp, key=itemgetter(int(input()))):
    print (*j)

