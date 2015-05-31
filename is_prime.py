#!/usr/bin/python
def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2,x):
            if x % i == 0:
               return False
               break
        else:
            return True
its = int(raw_input('please type a num > 2, will return prime in this range : '))
for y in range(1,its):
    if is_prime(y) == True:
       print y, 
