import re
n = int(input())
for i in range(n):
    if re.findall(r'^\b[4|5|6]{1}[0-9]{3}\-?[0-9]{4}\-?[0-9]{4}\-?[0-9]{4}\b$', input()):
        print('Valid')
    else:
        print('Invalid')
