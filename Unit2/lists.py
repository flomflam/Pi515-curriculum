# myList = ["spring", "summer", "fall", "winter"]
# print(myList) 

# lastItem = myList[len(myList)-1]
# print(len(myList))
# print(lastItem)

# L1 = ["October", 31, "Halloween", True]
# print(L1)

# months = list(("June", "July", "August"))
# print(months)

numList = [1, 1, 2, 3, 5, 8, 13, 21]
print(numList)

# print(numList[0:3])
# print(numList[4:])

numList[0] = 0

print(numList)

#max = -10000
#min = 10000 
#min = numList[0]
#max = numList[0]

firsttime = True
# Kevins code :)
for x in numList: 
#  if(min < x):
#    print(x)
  if firsttime:
      min = x
      max = x
      firsttime = False
  if(max < x):
    max = x
  if(min > x):
 #   print(x, "This is the smallest so far")
    min = x

print("This is the min ", min)
print("This is the max ", max)
