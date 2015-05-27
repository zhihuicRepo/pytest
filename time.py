#!/usr/bin/python
from datetime import datetime
now = datetime.now()
print '%s-%s-%s %s:%s:%s' %(now.year,now.month,now.day,now.hour,now.minute,now.second)


# Add your code below!
try:
     guess_row = int(raw_input("Guess Row: "))
     guess_col = int(raw_input("Guess Col: "))
     print guess_row,guess_col
except ValueError:
     print ('please input a num')
