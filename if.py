#!/usr/bin/python
from datetime import datetime
now = datetime.now()
nowtime = '%s-%s-%s %s:%s:%s' %(now.year,now.month,now.day,now.hour,now.minute,now.second)
""" string table space is %s,float table space is %f,int table space is %d """
def phonenum(wuhan,hangzhou,wenzhou):
    print "%d,%d,%d" %(wuhan,hangzhou,wenzhou)
phonenum(15002753590,18667198692,18958938816)
phonenum(1.23,12.9,123)
str1 = raw_input("please type your name : ")
if str1 == 'chenzh' :
    print str(str1),nowtime
elif str1 == '':
    print 'is null'
else : 
    print str(str1),nowtime,'you type fault'
