# Random Number Generator Guessing Game
# Three levels of difficulty
# Easy: 1-10
# Medium: 1-50
# Hard: 1-100
# Wins and loses for each level will be put into lists to display upon ending the game

import random
import tkinter as tk
from tkinter import *
from tkinter import ttk

# tkinter
window = tk.Tk()
window.title('Number Guessing Game')

window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], minsize=50, weight=1)
window.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], minsize=50, weight=1)

lbl = tk.Label(text='Would you like to play a number guessing game?')
lbl.grid(row=0, columnspan=9)

btn_y = tk.Button(
    master=window,
    text='Yes',
)
btn_y.grid(row=1, column=2)

btn_n = tk.Button(
    text='No',
)
btn_n.grid(row=1, column=6)

window.mainloop()


def start_game():
    play = input(
        'Would you like to play a number guessing game? (Enter yes or no) ')
    if play.lower() == 'yes':
        difficulty = input('Please enter Easy, Medium or Hard. ')
        if difficulty.lower() == 'easy':
            start_easy()
        elif difficulty.lower() == 'medium':
            start_medium()
        elif difficulty.lower() == 'hard':
            start_hard()
        else:
            print('Please enter Easy, Medium, or Hard to continue. ')
    else:
        print('Maybe next time!')

# Easy: 1-10,


a = 0
games_easy = [a]
wins_easy = 0
loss_easy = 0


def start_easy():
    global a, games_easy, wins_easy, loss_easy
    guesses_easy = 0
    rand_num = random.randint(1, 10)
    wanna_play = input(
        f'Are you ready to play the Easy level guessing game?'
        '(Enter Yes/No): ')
    print("You have 3 guesses")

    def show_score_easy():
        if wins_easy == 0 and loss_easy == 0:
            print('No games have been played yet.')

        elif wins_easy == 0 and loss_easy >= 1:
            print(
                f'You have lost ' + str(loss_easy) +
                ' game(s) out of ' + str(max(games_easy)) + ' game(s).')

        elif loss_easy == 0 and wins_easy >= 1:
            print(f'You have won ' + str(wins_easy) +
                  ' game(s) out of ' + str(max(games_easy)) + ' game(s)')

        else:
            print(f'You have played ' + str(max(games_easy)) + ' games with ' +
                  str(wins_easy) + ' win(s) and ' + str(loss_easy) + ' loss(es).')

    if wanna_play.lower() != 'yes':
        print('Maybe next time!')
        exit()
    else:
        show_score_easy()

    while wanna_play.lower() == 'yes':
        if guesses_easy == 3:
            a += 1
            loss_easy += 1
            games_easy.append(a)
            print("You've run out of guesses!")
            start_game()
        try:
            guess = int(input('Pick a number between 1 and 10: '))
            if guess < 1 or guess > 10:
                raise ValueError(
                    'Please guess a number between 1 and 10')

            guesses_easy += 1

            if guess == rand_num:
                a += 1
                wins_easy += 1
                games_easy.append(a)
                print('Nice! You got it!')
                print(f'It took you ' + str(guesses_easy) + ' attempts.')
                wanna_play = input(
                    'Would you like to play again? (Enter Yes/No): ')
                if wanna_play.lower() != 'yes':
                    print('Later!')
                    break
                else:
                    guesses_easy = 0
                    rand_num = random.randint(1, 10)
                    show_score_easy()
                    continue
            else:
                if guess > rand_num:
                    print('It\'s lower')
                elif guess < rand_num:
                    print('It\'s higher')

        except ValueError as err:
            print('Oh no!, that is not a valid value. Try again...')
            print(err)

# Medium 1-50


b = 0
games_medium = [b]
wins_medium = 0
loss_medium = 0


def start_medium():
    global b, games_medium, wins_medium, loss_medium
    guesses_medium = 0
    rand_num = random.randint(1, 50)
    wanna_play = input(
        'Are you ready to play the medium level guessing game?    (Enter Yes/No): ')
    print("You have 5 guesses")

    def show_score_medium():
        if wins_medium == 0 and loss_medium == 0:
            print('No games have been played yet.')

        elif wins_medium == 0 and loss_medium >= 1:
            print(
                f'You have lost ' + str(loss_medium) +
                ' game(s) out of ' + str(max(games_medium)) + ' game(s).')

        elif loss_medium == 0 and wins_medium >= 1:
            print(
                f'You have won ' + str(wins_medium) +
                ' game(s) out of ' + str(max(games_medium)) + ' game(s)')
        else:
            print(
                f'You have played ' + str(max(games_medium)) +
                ' games with ' + str(wins_medium) + ' win(s) and '
                + str(loss_medium) + ' loss(es).')

    if wanna_play.lower() != 'yes':
        print('Maybe next time!')
        exit()
    else:
        show_score_medium()

    while wanna_play.lower() == 'yes':
        if guesses_medium == 5:
            b += 1
            loss_medium += 1
            games_medium.append(b)
            print("You've run out of guesses!")
            start_game()
        try:
            guess = int(input('Pick a number between 1 and 50: '))
            if guess < 1 or guess > 50:
                raise ValueError(
                    'Please guess a number between 1 and 50')

            guesses_medium += 1

            if guess == rand_num:
                b += 1
                wins_medium += 1
                games_medium.append(b)
                print('Nice! You got it!')
                print(f'It took you ' + str(guesses_medium) + ' attempts.')
                wanna_play = input(
                    'Would you like to play again? (Enter Yes/No): ')
                if wanna_play.lower() != 'yes':
                    print('Later!')
                    break
                else:
                    guesses_medium = 0
                    rand_num = random.randint(1, 50)
                    show_score_medium()
                    continue
            else:
                if guess > rand_num:
                    print('It\'s lower')
                elif guess < rand_num:
                    print('It\'s higher')

        except ValueError as err:
            print('Oh no!, that is not a valid value. Try again...')
            print(err)

# Hard 1-100


c = 0
games_hard = [c]
wins_hard = 0
loss_hard = 0


def start_hard():
    global c, games_hard, wins_hard, loss_hard
    guesses_hard = 0
    rand_num = random.randint(1, 100)
    wanna_play = input(
        f'Are you ready to play the Hard level guessing game?'
        '(Enter Yes/No): ')
    print("You have 10 guesses")

    def show_score_hard():
        if wins_hard == 0 and loss_hard == 0:
            print('No games have been played yet.')

        elif wins_hard == 0 and loss_hard >= 0:
            print(f'You have lost ' + str(loss_hard) +
                  ' game(s) out of ' + str(max(games_hard)) + ' game(s).')

        elif loss_hard == 0 and wins_hard >= 1:
            print(f'You have won ' + str(wins_hard) +
                  ' game(s) out of ' + str(max(games_hard)) + ' game(s)')

        else:
            print(f'You have played ' + str(max(games_hard)) + ' games with ' +
                  str(wins_hard) + ' win(s) and ' + str(loss_hard) + ' loss(es).')

    if wanna_play.lower() != 'yes':
        print('Maybe next time!')
        exit()
    else:
        show_score_hard()

    while wanna_play.lower() == 'yes':
        if guesses_hard == 10:
            c += 1
            loss_hard += 1
            games_hard.append(c)
            print("You've run out of guesses!")
            start_game()
        try:
            guess = int(input('Pick a number between 1 and 100: '))
            if guess < 1 or guess > 100:
                raise ValueError(
                    'Please guess a number between 1 and 100')

            guesses_hard += 1

            if guess == rand_num:
                c += 1
                wins_hard += 1
                games_hard.append(c)
                print('Nice! You got it!')
                print(f'It took you ' + str(guesses_hard) + ' attempts.')
                wanna_play = input(
                    'Would you like to play again? (Enter Yes/No): ')
                if wanna_play.lower() != 'yes':
                    print('Later!')
                    break
                else:
                    guesses_hard = 0
                    rand_num = random.randint(1, 100)
                    show_score_hard()
                    continue
            else:
                if guess > rand_num:
                    print('It\'s lower')
                elif guess < rand_num:
                    print('It\'s higher')

        except ValueError as err:
            print('Oh no!, that is not a valid value. Try again...')
            print(err)


if __name__ == '__main__':
    start_game()


# classes
level = ['Easy', 'Medium', 'Hard']


class level:
    def __init__(level_difficulty):
        level.hard = loss_hard
        level.medium = loss_medium
        level.easy = loss_easy
