# #Assigning a variable
# x = 5
# print(x)

# #Update a variable
# x = 10
# print(x)

# #Delete a variable
# #del x
# print(x)

# #Define multiple variables
# v1, v2, v3 = "red", "white", "blue"
# print(v1)
# print(v2)
# print(v3)

# #unpacking values
# colors = ["red", "white", "blue"]
# x, y, z, = colors
# print(x+y+z)

# #do some addition
# x=5
# y=10
# print(x+y)

# #join numbers and alphabetical fields
# x=2
# y="cats"
# print(x,y)

# DAY 2 START HERE #
#Data types
# greeting = "Hello World"
# dog = "beagle"
# someNumber = 25
# someFloat = 17.9

# print(type(greeting))
# print(type(dog))
# print(type(someNumber))
# print(type(someFloat))

#Number types
# v1 = -568
# v2 = 12.34
# v3 = 15e7
# v4 = 5j
# v5 = 3 + 6j
# print(v1, v2, v3, v4, v5)

# #Convert the following variables into floats, print them, and check the data type.
# x = 7
# y = 10
# x = float(x)
# y = float(y)
# print(x, type(x))
# print(y, type(y))
# # #Convert the following variables into into integers, print them, and check the data type.
# a = 18.9
# b = -3.5
# a = int(a)
# b = int(b)
# print(a, type(a))
# print(b, type(b))
# #Convert the following variables in complex numbers, print them, and check the data type.
# v1 = 19.5
# v2 = -301
# v1 = complex(v1)
# v2 = complex(v2)
# print(v1, type(v1))
# print(v2, type(v2))

# #generate random numbers
import random
print('x')
print(random.random())
print(random.randrange(1, 100))

#Exercises
#1. Define variable someNum with value 7.5. Print the data type of
#   someNum. Convert it into an integer and print it. Convert it into a
#   complex number and print it
#2. Define variable x as a random integer between the values of 1 and 100.
#   Print variable x

#1
#someNum=7.5
#print(type(someNum))
#someNum=int(someNum)
#print(someNum)
#someNum=complex(someNum)
#print(someNum)

#2
#x=random.randrange(1,100)
#print(x)