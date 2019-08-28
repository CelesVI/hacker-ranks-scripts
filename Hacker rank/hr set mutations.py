from sys import stdin
a = int(input())
seta = set(list(map(int, stdin.readline().split())))
cant = int(input())
for i in range(0, cant):
    linea = stdin.readline().split()
    if (linea[0] == "intersection_update"):
        setb = {int(linea[1])}
        seta.intersection_update(setb)
        print(' '.join(list(map(str,seta))))
        
    elif (linea[0] == "update"):
        setb = {int(linea[1])}
        seta.update(setb)
        print(' '.join(list(map(str,seta))))
        
    elif (linea[0] == "symmetric_difference_update"):
        setb = {int(linea[1])}
        seta.symmetric_difference_update(setb)
        print(' '.join(list(map(str,seta))))
        
    elif (linea[0] == "difference_update"):
        setb = {int(linea[1])}
        seta.difference_update(setb)
        print(' '.join(list(map(str,seta))))

print(sum(list(seta)))
        
