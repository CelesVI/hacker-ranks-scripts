from sys import stdin

dic = {}
cant = int(input())
for i in range(0, cant):
    linea = stdin.readline().split()
    key, values = linea[0], linea[1:]
    for j in range (0, len(values)):
        values[j] = float(values[j])
    dic[key]= values

name = input()
avg = 0
suma = 0

if name in dic.keys():
    valores = dic[name]
    for k in range(0,len(valores)):
        suma += valores[k]
    avg = suma/len(valores)
    
print(format(avg, '.2f'))
    

