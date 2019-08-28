import re
regexPattern = r'^[7|8|9]{1}(\d{9})$'
for i in range(int(input())):
    if re.match(regexPattern, input()):
        print('YES')
    else:
        print('NO')
