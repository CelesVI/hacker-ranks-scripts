s = list(input())

value1 = False
value2 = False
value3 = False
value4 = False
value5 = False

for i in range(len(s)):
    if (s[i].isalnum()):
        value1 = True
    if (s[i].isalpha()):
        value2 = True
    if (s[i].isdigit()):
        value3 = True
    if (s[i].islower()):
        value4 = True
    if (s[i].isupper()):
        value5 = True
    
print(str(value1)+"\n"+str(value2)+"\n"+str(value3)+"\n"+str(value4)+"\n"+str(value5))

    
