from sys import stdin

list = []
amount = int(stdin.readline())
cont = 0
top1 = -101
top2 = -101
i = 0
addNum = stdin.readline().split()
for i in range(0, amount):
    convert=int(addNum[i])
    list.append(convert)
    if convert > top1:
        top1 = convert 
    if ((convert >= top2)&(convert < top1)):
        top2 = convert

print(top2)
