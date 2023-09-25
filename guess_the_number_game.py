def number_guess(number):
    from random import randrange
    computer_guess = randrange(1, 100)
    if number == computer_guess:
        result = 'You guessed it!'
    elif number < computer_guess:
        result = 'Too low!\nTry again!'
        if computer_guess - number < 10:
            result += '\n'
    else:
        result = 'Too high!\nTry again!'

    return result


command = input('Welcome to guess the number! press "enter" to continue or press "q" to quit:')
if command == 'q':
    raise SystemExit('Thanks for playing!')

elif command == '':
    while True:
        player_guess = int(input('Enter the number between 1 and 100: '))
        if number_guess(player_guess) == 'You guessed it':
            print(number_guess(player_guess))
            break
        else:
            print(number_guess(player_guess))
            continue


