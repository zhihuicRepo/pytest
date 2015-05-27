#!/usr/bin/python
name = [ 'james' , 'jason' , 'tom' , 25 , 30 , 50 ]
for x in name:
    if type(x) == str :
        print 'name : ',x
    elif type(x) == int:
        print 'age : ',x
    
    
def count_small(numbers):
    total = 0
    for n in numbers:
        if n < 10:
            total = total + 1
    return total

lost = [4, 8, 15, 16, 23, 42]
small = count_small(lost)
print small

for letter in "Codecademy" :
    print letter

print 
print 


