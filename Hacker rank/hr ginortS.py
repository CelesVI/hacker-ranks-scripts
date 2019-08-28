import string
parseL, parseU, parseE ,parseO = [], [], [], []
lower=set(list(string.ascii_lowercase))
upper=set(list(string.ascii_uppercase))
even=set([str(i) for i in range(9) if i % 2 == 0])
odd=set([str(i) for i in range(10) if i % 2 == 1])
palabra = input()
for i in palabra:
    if i in lower:
        parseL.append(i)
    elif i in upper:
        parseU.append(i)
    elif i in even:
        parseE.append(i)
    elif i in odd:
        parseO.append(i)
print(''.join(sorted(parseL)+sorted(parseU)+sorted(parseO)+sorted(parseE)))

#alternativa en dos líneas!!!
#myList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"
#print(*sorted(input(), key = myList.index), sep ="")
