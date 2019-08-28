from itertools import groupby


n = list(input())

a = []

print (a)

for key,group in groupby(n):
    print ((len(list(group)),key))
    

#'({},{})'.format
    
