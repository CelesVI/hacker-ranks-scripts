import string
abc = list(string.ascii_lowercase)

n = int(input())

corte = abc[0:n]
corte.reverse()

pattern = [('-'+corte[i]*(2*i+1)).center(n, '-') for i in range(n-1)]
print('\n'.join(pattern + [(abc[n-1]).center(n, '-')] + pattern[::-1]))
