from sys import stdin

N = int(input())

for i in range(N):
    listInt = []
    try:
        listInt = list(stdin.readline().split())
        print (int(listInt[0])//int(listInt[1]))
    except ValueError as e:
        print ("Error Code: "+str(e))
    except ZeroDivisionError as z:
        print ("Error Code: "+str(z))
        
