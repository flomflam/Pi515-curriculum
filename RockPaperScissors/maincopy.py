import random

list = ['rock', 'paper', 'scissors']
user_input = ''
computer_input = ''
winner = ''
i=0

# user input
while user_input not in list and i<3:
  user_input = input("Select rock, paper or scissors: ").lower()
  print("You chose: " + user_input)

  # input validation
  if user_input not in list:
    print("not a valid answer")
  i = i+1
  
if not user_input:
  print("You've used up all your tries")
else:
  while not winner:
    computer_input = random.choice(list)
    # computer_input = list[random.randrange(0,2)]
    print(computer_input)
    
    if user_input != computer_input:
      winner = "user"
      print(f)