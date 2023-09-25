from random import randrange

computer_guess = randrange(1, 100)


def number_guess(number):
    if number == computer_guess:
        result = 'You guessed it!'
    elif number < computer_guess:
        result = 'Too low!\n'
        if abs(computer_guess - number) < 10:
            result += 'You are getting closer!'
    else:
        result = 'Too high!\n'
        if abs(computer_guess - number) < 10:
            result += 'You are getting closer!\n '
    return result


command = input('Welcome to guess the number! press "enter" to continue or press "q" to quit:')

number_of_guesses = int(input('Please choose the number of guesses for your game: '))
if command == 'q':
    raise SystemExit('Thanks for playing!')
elif command == '':
    while number_of_guesses > 0:
        player_guess = input('Enter the number between 1 and 100: ')
        if player_guess.isdigit():
            player_guess = int(player_guess)
            number_of_guesses -= 1
            if player_guess == computer_guess:
                print(number_guess(player_guess))
                break
            else:
                print(number_guess(player_guess))
                print(f'Attempts remaining: {number_of_guesses}\n')
        elif player_guess == 'q':
            print('Thanks for playing!')
            break
        else:
            print('Invalid input!\nPlease try again.')
    else:
        print('You ran out of guesses!')

