# numSet = {7, 14, 21, 28}
# print(49 in numSet)
# print(7 in numSet)

# print(numSet)
# numSet.add(35)
# numSet.add(7)
# print(numSet)

# numSet2 = {42,49,56,63,70}
# numSet.update(numSet2)
# print(numSet)

# icecream = {'mint','chocolate','vanilla','strawberry','caramel'}
# icecream.remove('mint')
# icecream.discard('caramel')
# print(icecream)

##########
#if statements
a = 33
b = 200
c = 75

# if a < c and a < b:
# 		print ('both these conditions are true')
# if c > a and c > b:
# 	print ('at least one of these conditions is true')

# x = 50
# if x >10:
#   print("Above 10")
#   if x<20:
#     print('above 20')

# x = 15
# y = 5
# if x < y:
# 	print ('x is less than y')
# elif x > y:
#   print ('x is greater than y')

# x = 20
# y = 10
# if x > y:
# 	print ('x is greater than y')
# elif x < y:
#   print ('x is less than y')
# else:
#   print('They are equal')

###########
# While loops
# i = 1
# while i < 6:
#   print (i)
#   i = i + 1

# i = 1
# while i < 6:
#   while i <5:
#     print (i)
#     if i == 3:
#       break
#     i += 1
#   print("I am still going sam")
#   i += 1

# i= 7
# while i > 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

#########
# For Loops
# fruits = ['mango','cherry','pineapple', 'Kiwi']
# for fruit in fruits:
#   print(fruit)

# colors = ['red', 'yellow', 'green', 'blue', 'magenta', 'orange', 'turquoise']

# for color in colors:
#   print(color)
# print a certain statement for one object, but print something else for all the other objects

# for x in range (10):
# 	print (x)
# for x in range (2, 10):
# 	print (x)
# for x in range (3, 30, 3):
# 	print (x)

list = []
print(list)
for x in range(1, 101):
  if not x % 5 == 0:
    list.append(x)

print(list)

# for x in range (6, 17):
#   if x == 10:
#     break
#   print (x)
# else:
# 	print ('The loop is finished')

# CREATE list of different types of candy/pop/food
# Print out how many different candys/pop/food are in the list
# Print out a statement with each candy/pop/food using FOR LOOP
# Print out a different statement if you do not like the candy/pop/food
