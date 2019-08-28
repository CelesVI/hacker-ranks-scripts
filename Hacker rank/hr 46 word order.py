from collections import Counter

lista = []
a = int(input())

for _ in range(a):
    word = input()
    lista.append(word)

print(len(set(lista)))

cont = Counter(lista)
for key, value in cont.items():
    print(value, end = ' ')
