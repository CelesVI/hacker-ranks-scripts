from sys import stdin
a = int(input())
seta = set(list(map(int, stdin.readline().split())))
cant = int(input())
for i in range(0, cant):
    linea = stdin.readline().split()
    if (linea[0] == "pop"):
        seta.pop()
    elif (linea[0] == "remove"):
        seta.remove(int(linea[1]))
    elif (linea[0] == "discard"):
        seta.discard(int(linea[1]))
    else:
        print("Opción inválida")

print(sum(list(seta)))
