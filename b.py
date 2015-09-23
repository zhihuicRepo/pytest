import math
def polygon(a,b):
    n = float(a)
    s = float(b)
    area = (1.0/4*n*s**2)/math.tan(math.pi/n)
    return area

print polygon(5,7)
print polygon(7,3)


