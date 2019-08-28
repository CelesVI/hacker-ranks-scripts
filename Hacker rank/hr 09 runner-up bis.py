n = int(input())
arr = list(map(int, input().split()))
aset = set(arr)
arr = list(aset)
arr.sort(reverse=True)
print (arr[1])

