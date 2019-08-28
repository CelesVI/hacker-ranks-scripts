import calendar
import string
from sys import stdin

#Diccionario de los dias.
#days={0:'MONDAY', 1:'TUESDAY', 2:'WEDNESDAY', 3:'THURSDAY', 4:'FRIDAY', 5:'SATURDAY', 6:'SUNDAY'}

date = list(map(int, stdin.readline().split()))

#print (days.get(calendar.weekday(date[2],date[0],date[1])))

print (calendar.day_name[calendar.weekday(date[2],date[0],date[1])].upper())
