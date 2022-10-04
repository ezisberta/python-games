import random

def guess(cap_number):
    feedback = ''
    known_lower = 0
    known_higher = cap_number
    user_ready = input(f'Think of a number from 0 to {cap_number} and I will guess it. Reply with R to start. ').lower()
    while feedback != 'c' and user_ready == 'r':
        if known_lower != known_higher:
            computer_guess = random.randint(known_lower, known_higher)
        else:
            computer_guess = known_lower
        feedback = input(f'Is {computer_guess} too high (H), too low (L) or correct (C)?').lower()
        if feedback == 'h' :
                known_higher = computer_guess - 1
        if feedback == 'l' :
                known_lower = computer_guess + 1

    print(f'HURRAY! I guessed it, it is {computer_guess}!')

guess(9)