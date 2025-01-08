"""
File: hangman.py
Name: Ian
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    First, choose random word for hangman game.
    Hangman game with N_TURNS attempts start!
    """
    word = random_word()
    hangman(word)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def hangman(word):
    """
    :param word: str, the chosen word for hangman game
    """
    count = N_TURNS  # track the number of attempts
    dash = ''
    for ch in word: # draw - according to the length of the random chosen word
        dash += '-'
    print('The word looks like: ' + dash)
    print('You have ' + str(count) + ' wrong guesses left.')
    guess = input('Your guess: ')
    length = int(len(guess))
    guess_uppercase = guess.upper()  # transform to UPPERCASE
    while True:
        if guess.isdigit() or (length > 1):  # digit and multi-alphabet are illegal
            print('Illegal format')
            guess = input('Your guess: ')
            length = int(len(guess))
            guess_uppercase = guess.upper()  # transform to UPPERCASE
        elif guess_uppercase in word:  # the case that the guess alphabet in the word
            ans = ''
            for j in range(len(word)):
                ch = word[j]
                if ch != guess_uppercase:
                    if dash[j] == word[j]:  # concat prior successfully guessed alphabet, which store in variable: data
                        ans += dash[j]
                    else:  # concat '-'
                        ans += '-'
                else:  # concat the successfully guessed alphabet
                    ans += guess_uppercase
            if ans != word:
                print('The word looks like: ' + ans)
                print('You have ' + str(count) + ' wrong guesses left.')
                dash = ans
                guess = input('Your guess: ')
                length = int(len(guess))
                guess_uppercase = guess.upper()  # transform to UPPERCASE
            else:
                print('You are correct!')
                print('You win!!')
                break  # you win -> jump out the while loop
        else:  # the case that the guess alphabet not in the word and in the legal form
            print('There is no ' + guess_uppercase + "'" + 's in the word.')  # if guessed alphabet not in the word
            count -= 1  # subtract the attempts
            if count != 0:
                print('The word looks like: ' + dash)
                print('You have ' + str(count) + ' wrong guesses left.')
                guess = input('Your guess: ')
                length = int(len(guess))
                guess_uppercase = guess.upper()  # transform to UPPERCASE
            else:
                print('You are completely hung :(')
                break  # run out the number of attempts -> jump out the while loop
    print('The answer is: ' + word)











# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
