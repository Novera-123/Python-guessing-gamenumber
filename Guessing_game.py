import random
from art import logo
print(logo)

easy_level = 5
hard_level = 10

def compare_num(user_num,comp_num, turns):
    if user_num > comp_num:
        print("Too high")
        return turns -1
    elif user_num < comp_num:
        print("Too low")
        return turns -1
    else:
        print(f"YOU WIN. Game over. The answer was {comp_num}")
def difficulty_level():
    level = input("Please choose your difficulty level. type 'easy' or 'hard'").lower()
    if level == 'hard':
        return hard_level
    if level == 'easy':
        return easy_level
def game():
    print("Hello and welcome the the guessing game")
    print("I am thinking of a number between 1 and 100")

    comp_num = random.randint(1,100)
    #print(f"the num is {comp_num}")

    turns = difficulty_level()
    guess = 0
    while guess != comp_num:
        print(f"you have {turns} left to guess the number ")
        guess = int(input("Make a guess: \n"))
        turns = compare_num(guess,comp_num,turns)

        if turns == 0:
            print("Your turns are finished")
            return
        elif guess != comp_num:
            print("guess again")

game()


