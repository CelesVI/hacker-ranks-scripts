from itertools import permutations
from itertools import chain
from sys import stdin
import string
import textwrap

lista = list(stdin.readline().split())

newTuples = (list(permutations(sorted(lista[0]), int(lista[1]))))

for i in range(len(newTuples)):
    priLista = []
    for j in range(int(lista[1])):
        priLista.append(newTuples[i][j])
        
    print((''.join(priLista)))
