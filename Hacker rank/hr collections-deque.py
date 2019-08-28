from collections import deque
from sys import stdin
d = deque()
amount = int(input())
for i in range(amount):
    op = list(map(str, stdin.readline().split()))
    if op[0] == 'append':
        d.append(int(op[1]))
    elif op[0] == 'appendleft':
        d.appendleft(int(op[1]))
    elif op[0] == 'pop':
        d.pop()
    elif op[0] == 'popleft':
        d.popleft()
    else:
        break
print(*d, sep='\n')
