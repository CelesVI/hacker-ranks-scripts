import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    nombres = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if re.findall(r'(@(gmail.com))', emailID):
            nombres.append(firstName)
nombres = sorted(nombres)
print(*nombres, sep='\n')
            
