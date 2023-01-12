list = ['rock', 'paper', 'scissors']
user_input = ''
i=0

# user input
while user_input not in list and i<3:
  user_input = input("Select rock, paper or scissors: ").lower()
  print("You chose: " + user_input)

  # input validation
  if user_input not in list:
    print("not a valid answer")

  i = i+1
  print(i)
if i==3:
  print("You've used up all your tries")