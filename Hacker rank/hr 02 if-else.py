N = int(input())

if (N % 2 == 1):
    print ("Weird")
elif ((N % 2 == 0) & (N >= 2) & (N <= 5)):
    print("Not Weird")
elif ((N % 2 == 0) & (N >= 6) & (N <= 20)):
    print("Weird")
elif ((N % 2 == 0) & (N > 20)):
    print("Not Weird")

