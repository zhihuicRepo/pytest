#coding=utf-8
#!/usr/bin/python
a = 18
if a == 20:
 print "first，20 ,欢迎您hello world!";
elif a > 20:
 print 'a > 20 ';
else:
 print 'not >20 ';

def print_board(board):
    for row in board:
        print " ".join(row)
a = []
x = 1
for x in range(18):
    a.append(['http_' + str(400 + x)] )
    x += 1
print a
print pow(7)
#print_board(a)
