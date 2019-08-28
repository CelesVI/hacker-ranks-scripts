from sys import stdin
n = int(input())
conj = set(map(int, stdin.readline().split()))
op = int(input())
for i in range(op):
    op = list(map(str, stdin.readline().split()))
    if op[0] == 'intersection_update':
        setemp = set(map(int, stdin.readline().split()))
        conj.intersection_update(setemp)
    elif op[0] == 'update':
        setemp = set(map(int, stdin.readline().split()))
        conj.update(setemp)
    elif op[0] == 'symmetric_difference_update':
        setemp = set(map(int, stdin.readline().split()))
        conj.symmetric_difference_update(setemp)
    elif op[0] == 'difference_update':
        setemp = set(map(int, stdin.readline().split()))
        conj.difference_update(setemp)
    else:
        break
print(sum(list(conj)))
