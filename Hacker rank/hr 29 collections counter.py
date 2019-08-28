from sys import stdin
from collections import Counter
# myList = list(map(int,stdin.readline().split()))

numShoes = int(input())

myList = Counter(list(map(int,stdin.readline().split())))

sSelleds = int(input())
total = 0
newList = []
while sSelleds > 0:
    newList = list(map(int,stdin.readline().split()))
    if myList[newList[0]] > 0:
        total += newList[1]
        myList[newList[0]] -= 1
    sSelleds -= 1

print (total)
