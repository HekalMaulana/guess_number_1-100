import random


def generate_number():
    for i in range (2, 100):
        NUMBER.append(i)

    number_choice = random.choice(NUMBER)
    return number_choice\
# Generate number from between 1 and 100. Choice number

def easy_difficulty(health,number_choice):
    while health > 0:
        print(f"You have {health} attempts remaining to guess a number")
        make_guess = int(input("Make a guess: "))
        if make_guess == number_choice:
            return print(f"You Guess Right Number {make_guess}")
            # health -= health
        elif make_guess > number_choice:
            print("To High")
            health -= 1
        elif make_guess < number_choice:
            print("To Low")
            health -= 1
    return print("Game Over")
# Easy difficulty function

def hard_difficulty(health,number_choice):
    while health > 0:
        print(f"You have {health} attempts remaining to guess a number")
        make_guess = int(input("Make a guess: "))
        if make_guess == number_choice:
            return print(f"You Guess Right Number {make_guess}")
            # health -= health
        elif make_guess > number_choice:
            print("To High")
            health -= 1
        elif make_guess < number_choice:
            print("To Low")
            health -= 1
    return print("Game Over")
# Hard difficulty function

def play_game(number_choice):

    print("Welcome to the number guessing game!!")
    print("I'm thinking the number between 1 and 100")
    print(number_choice)


    difficulty_choose = input("Choose difficulty. Type 'easy' or 'hard' : ")
    if difficulty_choose == "easy":
        easy_difficulty(EASY,number_choice)
    elif difficulty_choose == "hard":
        hard_difficulty(HARD,number_choice)
    else:
        play_game(generate_number())
# Guess a number game

NUMBER = []
HARD = 5
EASY = 10



play_game(generate_number())


