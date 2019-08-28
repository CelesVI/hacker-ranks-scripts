import re
regexPattern = r'^([+-]?[0-9]+)*\.?[0-9][1-9]*$'
for i in range(int(input())):
    if re.match(regexPattern, input()):
        print('True')
    else:
        print('False')
    
