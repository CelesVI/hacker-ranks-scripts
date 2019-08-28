nombres = []
segundos = []
scores = set()
for _ in range(int(input())):
        name = input()
        score = float(input())
        nombres.append([name, score])
        scores.add(score)

second = sorted(scores)[1]
for name, score in nombres:
    if score == second:
        segundos.append(name)

for name in sorted(segundos):
    print(name, end= '\n')

