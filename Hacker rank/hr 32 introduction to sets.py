from sys import stdin

#Solución sin la firma.

#amount = int(input())
#num = set(map(lambda s: int(s) if s.isdigit() else s, stdin.readline().split()))
#suma = sum(num)
#total = round(suma/len(num), 3)
#print (total)

def average(array):
     #your code goes here
    return round(sum(set(array))/len(set(array)), 3)
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
