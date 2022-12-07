# # What is a list
# myList = ["spring", "summer", "fall", "winter"]
# print(myList) 

# # Length of a list
# lastItem = myList[len(myList)-1]
# print(len(myList))
# print(lastItem)

# Lists can contain any data types within the same list
# L1 = ["October", 31, "Halloween", True]
# print(L1)

# print(L1[1])
# print(L1[-3])
# print(L1[len(L1)-1])

# # # Can also create lists using a function
# months = list()
# print(months)


# # Accessing elements within a list
# numList = [1, 1, 2, 3, 5, 8, 13, 21]
# print(numList)

# # # Can print a range of items from the list
# print(numList[0:3])
# print(numList[4:])

# # can check if an item is in the list
# print(13 in numList)

# # Change an item in a list
# numList[0] = 0

# print(numList)

# # To add a new item without replacing anything already in the list
# numList.insert(34)
# print(numList)

# To specifically add an item to the end of a list
flavors = ["chocolate", "vanilla", "cookie dough", "bunny tracks", "cookies and creme"]


flavors2 = ["mint", "orange", "vanilla","bubblegum", "blueberry"]

#flavors.insert(0, "bubblegum")
#flavors.append("bubblegum")
flavors = flavors + flavors2
print(flavors)

flavors.remove("bunny tracks")
print(flavors)
flavors.pop(4)
print(flavors)


# print("vanilla" in flavors)
# print("vanilla" in flavors2)
# print("bubblegum" in flavors)
# print("bubblegum" in flavors2)



# flavors.append("strawberry")
# print(flavors)
# flavors2 = ["mint", "carmel"]
flavors.extend(flavors2)
# print(flavors)

# # To then remove a specific element
# flavors.remove("vanilla")
# print(flavors)
# # To remove whatever is at a certain index
# flavors.pop(2)
# print(flavors)

# Sort

# Copy

# Join


#max = -10000
#min = 10000 
#min = numList[0]
#max = numList[0]

# firsttime = True
# # Kevins code :)
# for x in numList: 
# #  if(min < x):
# #    print(x)
#   if firsttime:
#       min = x
#       max = x
#       firsttime = False
#   if(max < x):
#     max = x
#   if(min > x):
#  #   print(x, "This is the smallest so far")
#     min = x

# print("This is the min ", min)
# print("This is the max ", max)
