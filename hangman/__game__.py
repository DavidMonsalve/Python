import random
import os

def run():

    images = [
                '''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        /|   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        /|\  |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        /|\  |
        /    |
            |
        =========''', '''
        +---+
        |   |
        O   |
        /|\  |
        / \  |
            |
        ========='''
    ]

    database = [
        "PYTHON",
        "JAVASCRIPT",
        "PHP",
        "C"
    ]

    word = random.choice(database)
    spaces = ["_"] * len(word)

    attemps = 6

    while True:
        os.system("cls")
        for character in spaces:
            print(character, " ")
        print(images[attemps])
        print("attemps left: " + str(attemps))
        user_input = input("Choose a letter: ").upper()

        found = False

        for index, character in enumerate(word):
            if character == user_input:
                spaces[index] = user_input
                found = True

        if not found:
            attemps -= 1

        if "_" not in spaces:
            os.system("cls")
            print("you won. ")
            break
            input()

        if attemps == 0:
            os.system("cls")
            print("you lost. ")
            break
            input()


if __name__ == "__main__":
    run()
