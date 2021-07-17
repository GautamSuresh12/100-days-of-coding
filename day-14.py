import random
from art import vs
from art import logo
from game_data import data
from replit import clear

def format_data(account):
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(answer, a_follower_count, b_follower_count):
  if a_follower_count > b_follower_count:
    return answer == "a"
  else:
    return answer == "b"

print(logo)
is_game_over = True
score =  0
b = random.choice(data)

while is_game_over:
  
  a = b
  b = random.choice(data)

  while a == b:
    b = random.choice(data)

  print(f"Compare A : {a}")
  print(vs)
  print(f"Against B : {b}")

  answer = input("Who has more followers. Type 'A' or 'B': ").lower()

  a_follower_count = a["follower_count"]
  b_follower_count = b["follower_count"]
  is_correct = check_answer(answer, a_follower_count, b_follower_count)

  clear()

  if is_correct:
    score += 1
    print(f"You are right, your score is {score}")
  else:
    print(f"Sorry, That's wrong, Your final score : {score}")
    

  


  
    



