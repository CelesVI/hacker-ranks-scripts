from sys import stdin

s1 = int(input())

conjunto1 = set(list(map(int,stdin.readline().split())))

s2 = int(input())

conjunto2 = set(list(map(int,stdin.readline().split())))

inter = list(conjunto1.intersection(conjunto2))

print (len(inter))
