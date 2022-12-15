# # total gifts
# # how many of each gift

# day1 = 1
# day2 = 2
# day3 = 3
# day4 = 4

# par_counter = 0
# dove_counter = 0
# hen_counter = 0
# bird_counter = 0

# for day in range(1,5):
#   print("the day is:", day)
#   par_counter += day1
#   print("par_counter =", par_counter)

#   if day > 1:
#     dove_counter += day2
#     print("dove_counter =", dove_counter)
  
#   if day > 2:
#     hen_counter += day3
#     print("hen_counter =", hen_counter)

#   if day > 3:
#     bird_counter += day4
#     print("bird_counter =", bird_counter)

#   print("\n")

# total = par_counter+dove_counter+hen_counter+bird_counter
# print("Total number of gifts =",total)



gift_counters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for gift in range (1,13):
  for x in range(gift):
    gift_counters[x] += x+1
    
print(gift_counters)
total = 0

for counter in gift_counters:
  total = total + counter

print("total number of gifts:",total)