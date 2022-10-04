import random

def guess(cap_number):
    random_number = random.randint(0,cap_number)
    user_guess = ''
    while user_guess != random_number:
        user_guess = int(input(f'Guess an integer between 0 and {cap_number}: '))
        print(user_guess)
        if user_guess < random_number:
            print(f'Sorry, {user_guess} is too low, try again!')
        elif user_guess > random_number:
            print(f'Sorry, {user_guess} is too high, try again!')
    
    print('HURRAY! You have guessed the number!')

guess(9)