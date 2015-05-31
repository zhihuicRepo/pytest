#!/usr/bin/python
from datetime import datetime
now = datetime.now()
nowday = '%s-%s-%s %s:%s:%s' %(now.year,now.month,now.day,now.hour,now.minute,now.second)
for i in range(10):
    print nowday , i
    i += 1
    if i == 9:
        print nowday,'you are fault'
        break
