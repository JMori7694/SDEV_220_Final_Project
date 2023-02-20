# Random Number Generator Guessing Game
# Three levels of difficulty
# Easy: 1-10
# Medium: 1-50
# Hard: 1-100
# Wins and loses for each level will be put into lists to display upon ending the game

import random


def start_game():
    play: str = input(
        'Would you like to play a number guessing game? (Enter yes or no)')
    if play.lower == 'yes':
        difficulty: str = input('Please enter Easy, Medium or Hard.')
        if difficulty.lower == 'easy':
            start_easy()
#        elif difficulty.lower == 'medium':
#            start_medium()
#        elif difficulty.lower == 'hard':
#            start_hard()
        else:
            print('Please enter Easy, Medium, or Difficult to continue.')
    else:
        print('Maybe next time!')

# Easy: 1-10,


games_easy = []
wins_easy: int = 0
loss_easy: int = 0


def show_score_easy():
    if not wins_easy and loss_easy:
        print('No games have been played yet.')

    elif not wins_easy:
        print(f'You have lost ' + loss_easy +
              ' game(s) out of ' + games_easy + ' game(s).')

    elif not loss_easy:
        print(f'You have won ' + wins_easy +
              ' game(s) out of ' + {max(games_easy)} + ' game(s)')

    else:
        print(f'You have played ' + {max(games_easy)} + ' games with ' +
              wins_easy + ' win(s) and ' + loss_easy + ' loss(es).')


def start_easy():
    guesses_easy: int = 0
    rand_num = random.randint(1, 10)
    wanna_play: str = input(
        f'Are you ready to play the Easy level guessing game?'
        '(Enter Yes/No): ')

    if wanna_play.lower() != 'yes':
        print('Maybe next time!')
        exit()
    else:
        show_score_easy()

    while wanna_play.lower() == 'yes':
        try:
            guess = int(input('Pick a number between 1 and 10: '))
            if guess < 1 or guess > 10:
                raise ValueError(
                    'Please guess a number between 1 and 10')

            guesses_easy += 1

            if guess == rand_num:
                print('Nice! You got it!')
                print(f'It took you {guesses_easy} attempts')
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


if __name__ == '__main__':
    start_game()

# Medium 1-50


# Hard 1-100
