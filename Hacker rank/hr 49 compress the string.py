from itertools import groupby

n = list(input())

for key,group in groupby(n):
    print ('({},{})'.format(len(list(group)),key),end=' ')
    

#'({},{})'.format
    
