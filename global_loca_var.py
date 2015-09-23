# Example of a simple event-driven program

# CodeSkulptor GUI module
#import simplegui

num = 1
# Event handler
def tick():
    print num

def prinN2():
    num = 2
    return num
    
def prinN3():
    global num 
    num = 3
    return num

print num
prinN2()
print num
prinN3()
print num

# Register handler
#timer = simplegui.create_timer(1000, tick)


