# Random Number Generator Guessing Game
# Three levels of difficulty
# Easy: 1-10
# Medium: 1-50
# Hard: 1-100
# Wins and loses for each level will be put into lists to display upon ending the game

import random
# Medium 1-50



games_medium = []
wins_medium = 0
loss_medium = 0
def show_score_medium():
    global wins_medium
    global loss_medium

    if not wins_medium and loss_medium:
        print('No games have been played yet.')

    elif not wins_medium:
        print(f'You have lost {loss_medium} game(s) out of {games_medium}game(s).')

    elif not loss_medium:
        print(f'You have won {wins_medium} game(s) out of {max(games_medium)} game(s)')
    else:
        print(f'You have played {max(games_medium)} games with {wins_medium} win(s) and {loss_medium}loss(es).')
    if not wins_medium and loss_medium:
        print('No games have been played yet.')

    elif not wins_medium:
        print(f'You have lost {loss_medium}  game(s) out of {games_medium} game(s).')

    elif not loss_medium:
        print(f'You have won {wins_medium} game(s) out of {max(games_medium)}  game(s)')

    else:
        print(f'You have played ' + {max(games_medium)} + ' games with ' +
              wins_medium + ' win(s) and ' + loss_medium + ' loss(es).')

def start_medium():
    global wins_medium
    global loss_medium
    guesses_medium = 0
    rand_num = random.randint(1, 50)
    wanna_play = input('Are you ready to play the medium level guessing game?    (Enter Yes/No): ')
    print("You have 5 guesses")

    if wanna_play.lower() != 'yes':
        print('Maybe next time!')
        exit()
    else:
        show_score_medium()

    while wanna_play.lower() == 'yes':
        if guesses_medium == 5: 
            loss_medium += 1 

            print("You've run out of guesses!")
            break
        try:
            guess = int(input('Pick a number between 1 and 50: '))
            if guess < 1 or guess > 50:
                raise ValueError(
                    'Please guess a number between 1 and 50')

            guesses_medium += 1

            if guess == rand_num:
                wins_medium += 1 
                print('Nice! You got it!')
                print(f'It took you {guesses_medium} attempts')
                wanna_play = input(
                    'Would you like to play again? (Enter Yes/No): ')
                if wanna_play.lower() != 'yes':
                    print('Later!')
                    break
                else:
                    guesses_medium = 0
                    rand_num = random.randint(1, 50)
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

def show_score_hard():
    global wins_hard
    global loss_hard

    if not wins_hard and loss_hard:
        print('No games have been played yet.')

    elif not wins_hard:
        print(f'You have lost'+ loss_hard +
             'game(s) out of'+ games_hard +'game(s).')

    elif not loss_hard:
        print(f'You have won'+ wins_hard +
             'game(s) out of'+ {max(games_hard)} +'game(s)')

    else:
        print(f'You have played'+ {max(games_hard)} +'games with'+
              wins_hard +'win(s) and'+ loss_hard +'loss(es).')
    if not wins_hard and loss_hard:
        print('No games have been played yet.')

    elif not wins_hard:
        print(f'You have lost ' + loss_hard +
              ' game(s) out of ' + games_hard + ' game(s).')

    elif not loss_hard:
        print(f'You have won ' + wins_hard +
              ' game(s) out of ' + {max(games_hard)} + ' game(s)')

    else:
        print(f'You have played ' + {max(games_hard)} + ' games with ' +
              wins_hard + ' win(s) and ' + loss_hard + ' loss(es).')


def start_hard():
    guesses_hard = 0
    global loss_hard
    global wins_hard
    rand_num = random.randint(1, 100)
    wanna_play= input(
        f'Are you ready to play the medium level guessing game?'
        '(Enter Yes/No): ')
    print("You have 10 guesses") 

    if wanna_play.lower() != 'yes':
        print('Maybe next time!')
        exit()
    else:
        show_score_hard()

    while wanna_play.lower() == 'yes':
        if guesses_hard == 10: 
            loss_hard += 1 

            print("You've run out of guesses!")
            break
        try:
            guess = int(input('Pick a number between 1 and 100: '))
            if guess < 1 or guess > 100:
                raise ValueError(
                    'Please guess a number between 1 and 100')

            guesses_hard += 1

            if guess == rand_num:
                wins_hard += 1 
                print('Nice! You got it!')
                print(f'It took you {guesses_hard} attempts')
                wanna_play = input(
                    'Would you like to play again? (Enter Yes/No): ')
                if wanna_play.lower() != 'yes':
                    print('Later!')
                    break
                else:
                    guesses_hard = 0
                    rand_num = random.randint(1, 100)
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
            
def start_game():
    play = input(
        'Would you like to play a number guessing game? (Enter yes or no)')
    if play.lower() == 'yes':
        difficulty = input('Please enter Easy, Medium or Hard.')
        if difficulty.lower() == 'easy':
            start_easy()
        elif difficulty.lower() == 'medium':            
            start_medium()
        elif difficulty.lower() == 'hard':
            start_hard()
        else:
            print('Please enter Easy, Medium, or Difficult to continue.')
    else:
        print('Maybe next time!')

# Easy: 1-10,


games_easy = []
wins_easy = 0
loss_easy = 0


def show_score_easy():
    global wins_easy
    global loss_easy
    if not wins_easy and loss_easy:
        print('No games have been played yet.')

    elif not wins_easy:
        print(f"You have lost {loss_easy} game(s) out of  {games_easy}   game(s).")

    elif not loss_easy:
        print(f'You have won ' + wins_easy +
              ' game(s) out of ' + {max(games_easy)} + ' game(s)')

    else:
        print(f'You have played ' + {max(games_easy)} + ' games with ' +
              wins_easy + ' win(s) and ' + loss_easy + ' loss(es).')


def start_easy():
    global wins_easy
    global loss_easy
    guesses_easy = 0
    rand_num = random.randint(1, 10)
    wanna_play = input(
        f'Are you ready to play the Easy level guessing game?'
        '(Enter Yes/No): ')
    print("You have 3 guesses")

    if wanna_play.lower() != 'yes':
        print('Maybe next time!')
        exit()
    else:
        show_score_easy()

    while wanna_play.lower() == 'yes':
        if guesses_easy == 3:
            print("You've run out of guesses!")
            break
        try:
            guess = int(input('Pick a number between 1 and 10: '))
            if guess < 1 or guess > 10:
                raise ValueError(
                    'Please guess a number between 1 and 10')

            guesses_easy += 1

            if guess == rand_num:
                loss_easy += 1 
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



games_medium = []
wins_medium = 0
loss_medium = 0







# Hard 1-100
games_hard = []
wins_hard = 0
loss_hard = 0


def show_score_hard():
    global wins_hard
    global loss_hard

    if not wins_hard and loss_hard:
        print('No games have been played yet.')

    elif not wins_hard:
        print(f'You have lost'+ loss_hard +
             'game(s) out of'+ games_hard +'game(s).')

    elif not loss_hard:
        print(f'You have won'+ wins_hard +
             'game(s) out of'+ {max(games_hard)} +'game(s)')

    else:
        print(f'You have played'+ {max(games_hard)} +'games with'+
              wins_hard +'win(s) and'+ loss_hard +'loss(es).')
    if not wins_hard and loss_hard:
        print('No games have been played yet.')

    elif not wins_hard:
        print(f'You have lost ' + loss_hard +
              ' game(s) out of ' + games_hard + ' game(s).')

    elif not loss_hard:
        print(f'You have won ' + wins_hard +
              ' game(s) out of ' + {max(games_hard)} + ' game(s)')

    else:
        print(f'You have played ' + {max(games_hard)} + ' games with ' +
              wins_hard + ' win(s) and ' + loss_hard + ' loss(es).')


def start_hard():
    guesses_hard = 0
    global loss_hard
    global wins_hard
    rand_num = random.randint(1, 100)
    wanna_play= input(
        f'Are you ready to play the medium level guessing game?'
        '(Enter Yes/No): ')
    print("You have 10 guesses") 

    if wanna_play.lower() != 'yes':
        print('Maybe next time!')
        exit()
    else:
        show_score_hard()

    while wanna_play.lower() == 'yes':
        if guesses_hard == 10: 
            loss_hard += 1 

            print("You've run out of guesses!")
            break
        try:
            guess = int(input('Pick a number between 1 and 100: '))
            if guess < 1 or guess > 100:
                raise ValueError(
                    'Please guess a number between 1 and 100')

            guesses_hard += 1

            if guess == rand_num:
                wins_hard += 1 
                print('Nice! You got it!')
                print(f'It took you {guesses_hard} attempts')
                wanna_play = input(
                    'Would you like to play again? (Enter Yes/No): ')
                if wanna_play.lower() != 'yes':
                    print('Later!')
                    break
                else:
                    guesses_hard = 0
                    rand_num = random.randint(1, 100)
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


