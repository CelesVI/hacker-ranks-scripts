from collections import Counter
comunes = list((Counter(sorted(input())).most_common(3)))
for i in comunes:
    print(str(i[0])+' '+str(i[1]))


