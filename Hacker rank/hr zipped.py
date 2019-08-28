from sys import stdin
students = []
n, x = map(int, input().split())
for i in range(x):
    subject1=list(map(float, stdin.readline().split()))
    students.append(subject1)
newStu=list(zip(*students))
prom=map(lambda i: sum(i)/x, newStu)
print(*prom, sep='\n')
