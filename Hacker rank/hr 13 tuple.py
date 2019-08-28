from sys import stdin

cant = int(input())
linea = stdin.readline().split()
num = [int(i) for i in linea]

tupla = tuple(num)

print (hash( (tupla) ))


