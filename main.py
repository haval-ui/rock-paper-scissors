import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



user_choice=int(input("input 0 for paper, 1 for rock, 2 for scissors :"))
com_choice=random.randint(0,2)
print(com_choice)
if user_choice==0:
  print(paper)
elif user_choice==1:
  print(rock)
elif user_choice==2:
  print(scissors)


if com_choice==0:
  print(paper)
elif com_choice==1:
  print(rock)
elif com_choice==2:
  print(scissors)


if user_choice==com_choice:
  print("that is an draw !!")
elif user_choice==0 and com_choice==1:
  print("you win!! ")
elif user_choice==1 and com_choice==0:
  print("computer  win!! ")
elif user_choice==0 and com_choice==2:
  print("com wins!! ")
elif user_choice==2 and com_choice==0:
  print("you win!! ")
elif user_choice==1 and com_choice==2:
  print("you win!! ")
elif user_choice==2 and com_choice==1:
  print("com wins!! ")