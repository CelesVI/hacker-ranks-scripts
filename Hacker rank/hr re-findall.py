import re
consonants = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
vowels = 'AEIOUaeiou'
i = [i for i in re.findall(r'(\w+)(consonants, vowels, consonants){2,})', str(input()))]
print ('\n'.join(i or ['-1']))


