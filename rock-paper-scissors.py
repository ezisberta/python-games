import random

def play():
    user = input("'R' for rock, 'P' for paper, 'S' for scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])
    letter_to_words = {'r': 'rock', 'p':'paper', 's': 'scissors'}

    print(f'I choose {letter_to_words[computer]}.')

    if user == computer:
        return 'We have a tie!'
    elif user == 'p' and computer == 'r' or user == 's' and computer == 'p' or user == 'r' and computer == 's':
        return 'CONGRATULATIONS! You won!'
    else:
        return 'YEYY! I won!'

print(play())