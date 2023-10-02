
def get_user_choice():
  while True:
    user_choice=input("Enter your choice  (rock, paper, or scissors):").strip().lower()
    #strip() is same as trim() in js
    #lower()==toLowerCase()
    if user_choice in ['rock','paper', 'scissor']:
      return user_choice
    else:
         print("Invalid choice. Please choose rock, paper, or scissors.")

import random

def get_computer_choice():
  choices=['rock','paper', 'scissor']
  computer_choice=random.choice(choices)
  return computer_choice

a=get_computer_choice()
print(a)

def determine_choice(user,comp):
  if user==comp:
    return "draw"
 
    
  elif user=='rock' and comp=='scissor' or user=='scissor' and comp=='paper' or user=='paper' and comp=='rock' :
    return "user"
  else :
    return "computer"
 

    
a=determine_choice(get_user_choice(),get_computer_choice())
print(a)   

def update_score(winner, scores):
  if winner=='user':
    scores['user']+=1
  elif winner=='computer':
    scores['computer']+=1
  else:
    scores['draw']+=1
    
  return scores

a=update_score(determine_choice(get_user_choice(),get_computer_choice()),{'user':0, 'computer':0,'draw':0})
print(a,"*********************")