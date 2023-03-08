# ROCK, PAPPER, SCISSORS GAME

rock = """
     _______
 ---'   ____)
       (_____)
       (_____)
       (____)
 ---.__(___)
 """

# Paper
paper = """
      _______
 ---'    ____)____
            ______)
           _______)
          _______)
 ---.__________)
 """

# Scissors
scissors = """
     _______
 ---'   ____)____
           ______)
        __________)
       (____)
 ---.__(___)
 """
import random
print("Welcome to the rock, paper, scissors game\nPress 0 for rock, 1 for scissors and 2 for paper.")
choice = int(input("Choose your hand\n"))
ai = random.randint(0, 2)
print(ai)
if choice == 0 and ai == 1:
    print(f"You chose\n{rock}\n AI: {paper}\nYou lose")
elif choice == 1 and ai == 0:
    print(f"You chose\n{paper}\n AI: {rock}\nYou win")
elif choice == 1 and ai == 2:
    print(f"You chose\n{paper}\n AI: {scissors}\nYou lose")
elif choice == 2 and ai == 1:
    print(f"You chose\n{scissors}\n AI: {paper}\nYou win")
elif choice == 0 and ai == 2:
    print(f"You chose\n{rock}\n AI: {scissors}\nYou win")
elif choice == 2 and ai == 0:
    print(f"You chose\n{scissors}\n AI: {rock}\nYou win")
elif choice == 0 and ai == 0:
    print(f"You chose\n{rock}\n AI: {rock}\nIts a draw")
elif choice == 1 and ai == 1:
    print(f"You chose\n{paper}\n AI: {paper}\nIts a draw")
elif choice == 2 and ai == 2:
    print(f"You chose\n{scissors}\n AI: {scissors}\nIts a draw")
else:
    print("Error...try again")
