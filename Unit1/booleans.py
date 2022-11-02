#Booleans
#Can print out if a math statement is true or false
print(10>9)
print(10==9)


#Can also determine if string are found within other strings
someTxt = "Red is my favorite color."
print("red" in someTxt)


#Run different code depending on if its true or false
a = 200
b = 200
if b < a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# if a == b:
#   print("yay for indenting")
# else:
#   print("nothing")
# this is what is known as an if else statement

  
#Everything can be a boolean!
print(bool("Helpicanttype"))
print(bool(21))
print(bool(()), bool([]), bool({}), bool(0), bool(None), bool(False), bool(""))


#Responses can be saved off in what is known as a function
def function():
 return False
  
if function():
 print('Yes')
else:
 print('No')

  
#Can verify if a type is what you expect or not and get a boolean value back
x = 200
print(isinstance(x, str))
print(isinstance(x, int))