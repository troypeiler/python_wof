import random
import emoji
import os

with open("countries.txt", "r") as f:
    contents = f.read().split("\n")

game_countries = random.sample(contents, 3)
while game_countries:

    game_country = game_countries.pop()

    display = ["_"] * len(game_country)

    if " " in game_country:
        for index, value in enumerate(game_country):
            if value == " ":
                display[index] = " "

    guesses = 0

    while "_" in display:
        print(*display)
        guess = input("What is your guess?: ")

        os.system("cls")

        if guess.isalpha():

            if guess in game_country:
                print(f"correct!{emoji.emojize(':thumbs_up:')}\n")
                for index, value in enumerate(game_country):
                    if value == guess:
                        display[index] = guess
            else:
                print(f"wrong guess {emoji.emojize(':disappointed_face:')}\n")

        else:
            print("guess not in the alphabet, try again\n")

        guesses += 1

    print(f"you guessed the country {game_country} it took you {guesses} guesses")