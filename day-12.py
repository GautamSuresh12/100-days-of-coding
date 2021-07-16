#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo
print (logo)

easy_level_turns = 10
hard_level_turns = 5

turns = 0
def check_answer(guess, answer, turns):
  """ checks answer against guess, returns the number of turns remaining"""
  if guess > answer:
    print("Too High")
    return turns - 1
  elif guess < answer:
    print("Too Low")
    return turns - 1
  else:
    print(f"Answer is correct :{answer}") 

def set_difficulty():
  level = input("Choose the difficulty. Type 'easy' or 'hard' ")
  if level == "easy":
    return easy_level_turns 
  else:
    return hard_level_turns

       
def game():
  print("Welcome to the Number Guessing Game")
  print("I'm Thinking of a number between 1 to 100")
  answer = random.randint(1, 100)

  turns = set_difficulty()
  
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number")

    guess = int(input("Make a Guess: "))

    
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("you have run out of guesses, You lose")
      return
game()
