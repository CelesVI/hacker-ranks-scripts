from sys import stdin
lista = []
cant = int(input())
for i in range(0, cant):
    linea = stdin.readline().split()
    if (linea[0] == "insert"):
        lista.insert(int(linea[1]), int(linea[2]))
    elif (linea[0] == "print"):
        print(lista)
    elif (linea[0] == "remove"):
        try:
            lista.remove(int(linea[1]))
        except ValueError:
            print("El valor no está en la lista")
    elif (linea[0] == "append"):
        lista.append(int(linea[1]))
    elif (linea[0] == "sort"):
        lista.sort()
    elif (linea[0] == "pop"):
        try:
            lista.pop()
        except IndexError:
            print("Fuera del rango")
    elif (linea[0] == "reverse"):
        lista.reverse()
    else:
        print ("Opcioón inválida")
