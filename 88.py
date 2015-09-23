def median(numList):
    if numList != None:
       a = numList.sort()
       b = len(a)
       c = (b+1)/2
       d = b/2
       if b == 1:
          total = a[0]
       elif b%2 == 1:
          total = a[c]
       else:
          total = (a[d] + a[d+1] )/2.0
       return total
    
print median([1,2,3,4])
