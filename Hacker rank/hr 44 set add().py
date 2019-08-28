lista = []

a = int(input())

for _ in range(a):
    word = input()
    lista.append(word)

print(len(set(lista)))
