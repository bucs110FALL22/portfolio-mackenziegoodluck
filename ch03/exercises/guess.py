import random

num = random.randrange(1,11)
num_guesses = 0 
correct_guesses = False

for i in range(3):
  guess_num = int(input("Please enter a guess:"))
  #num_guess = num_guesses + 1
  num_guesses += 1
  if guess_num > num:
    print("your guess is too high")
  elif guess_num < num:
    print("your guess is too low")
  else:
    print("correct!")
    correct_guess = True

  print( "It took you", num_guesses, "to get it right")
    
