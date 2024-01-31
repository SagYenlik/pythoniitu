#Syntax
#Exercise 1
print("Hello world")

#Exercise 2
if 5 > 2:
    print("YES")
 
#Comments   
#Exercise 1
#This is a comment

#Exercise 2
'''
this is a comment 
written in more
than just one line'''

#Variables
#Exercise 1
carname= "Volvo"

#Exercise 2
x=50

#Exercise 3
x=5
y=10
print(x+y)

#Exercise 4
x=5
y=10
z=x+y
print(z)

#Exercise 5
x, y, z = "Orange", "Banana", "Cherry"

#Exercise 6
x=y=z="Orange"

#Exercise 7
def myfunc():
    global x
x = "fantastic"

#DataTypes
#Exercise 1
x = 5
print(type(x))

int

#Exercise 2
x = "Hello World"
print(type(x))

str

#Exercise 3
x = 20.5
print(type(x))

float

#Exercise 4
x = ["apple", "banana", "cherry"]
print(type(x))

list

#Exercise 5
x = ("apple", "banana", "cherry")
print(type(x))

tuple

#Exercise 6
x = {"name" : "John", "age" : 36}
print(type(x))

dict

#Exercise 7
x = True
print(type(x))

bool

#Numbers
#Exercise 1
x = 5
x = float(x)

#Exercise 2
x = 5.5
x = int(x)

#Exercise 3
x = 5
x = complex(x)