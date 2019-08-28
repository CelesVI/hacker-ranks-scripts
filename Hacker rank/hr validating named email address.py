import re
from sys import stdin

a = int(input())
for i in range(a):
    lista = list(map(str, stdin.readline().split()))
    if re.findall(r'<[a-z|A-Z]{1}[a-zA-Z0-9|.|_|-]+\@[a-zA-Z]+\.[a-zA-Z]{1,3}>', lista[1]):
        print(lista[0]+' '+lista[1])

#[A-Za-z](\w|_|-|\.)
#[a-z|A-Z]{1}[a-zA-Z0-9._%+-]

