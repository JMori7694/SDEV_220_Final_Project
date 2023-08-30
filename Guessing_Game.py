# Random Number Generator Guessing Game
# Three levels of difficulty
# Easy: 1-10
# Medium: 1-50
# Hard: 1-100
# Wins and loses for each level will be put into lists to display upon ending the game

import random


def start_game():
    play: str = input(
        'Would you like to play a number guessing game? (Enter yes or no) ')
    if play.lower() == 'yes':
        difficulty: str = input('Please enter Easy, Medium or Hard. ')
        if difficulty.lower() == 'easy':
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


n = 0
games_easy = [n]
wins_easy: int = 0
loss_easy: int = 0


def start_easy():
    global n, games_easy, wins_easy, loss_easy
    guesses_easy: int = 0
    rand_num = random.randint(1, 10)
    wanna_play: str = input(
        f'Are you ready to play the Easy level guessing game?'
        '(Enter Yes/No): ')
    print("You have 3 guesses.")

    def show_score_easy():
        if wins_easy == 0 and loss_easy == 0:
            print('No games have been played yet.')

        elif wins_easy == 0 and loss_easy >= 1:
            print(f'You have lost ' + str(loss_easy) +
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
            n += 1
            games_easy.append(n)
            loss_easy += 1
            print('You ran out of guesses!')
            return games_easy
        try:
            guess = int(input('Pick a number between 1 and 10: '))
            if guess < 1 or guess > 10:
                raise ValueError(
                    'Please guess a number between 1 and 10')

            guesses_easy += 1

            if guess == rand_num:
                n += 1
                wins_easy += 1
                games_easy.append(n)
                print('Nice! You got it!')
                print(f'It took you {guesses_easy} attempts')
                wanna_play = input(
                    'Would you like to play again? (Enter Yes/No): ')
                if wanna_play.lower() != 'yes':
                    print('Later!')
                    return games_easy
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
