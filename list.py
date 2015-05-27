#!/usr/bin/python
backpack = ['taobao','jason','james','xylophone', 'dagger', 'tent', 'bread loaf']
print backpack
print backpack[0]
print backpack[1:3]
print backpack[1:]
print backpack[-1]
print backpack[-3:]
backpack.remove('xylophone')
print backpack


lloyd = {
    "name": "Lloyd",
    "homework": [],
    "quizzes": [],
    "tests": []
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
lloyd["homework"] = [ 90.0, 97.0, 75.0, 92.0 ]
lloyd["quizzes"] = [ 88.0, 40.0, 94.0 ]
lloyd["tests"] = [ 75.0, 90.0 ] 
students = [ lloyd , alice , tyler]
print students
for x in students:
    print x["name"]
    print x["homework"]
    print x["quizzes"]
    print x["tests"]
