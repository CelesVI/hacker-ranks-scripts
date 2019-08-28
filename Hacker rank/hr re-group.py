import re
##from sys import stdin
##s = stdin.readline().split()
m = re.search(r'([a-zA-Z0-9])\1+' , input().strip())

print(m.group(1) if m else -1)
