python_students = []
cant = int(input())
lowest1 = 101.00
lowest2 = 101.00
lname1 = ' '
lname2 = ' '
lname2bis = ' '

for i in range(0, cant):
    lista = []
    name = input()
    score = float(input())
    lista.append(name)
    lista.append(score)
    python_students.append(lista)

python_students.sort()

for (j, (name1,score1)) in enumerate(python_students):
    if (score1 <= lowest1):
        lowest2 = lowest1
        lowest1 = score1
    elif ((score1 > lowest1) & (score1 <= lowest2)):
        lowest2 = score1

for (k, (name2,score2)) in enumerate(python_students):
    if (score2 == lowest2):
        print(name2)

    
    
