import random
from random_word_list import words

def hangman(words):
    hidden_word = random.choice(words).upper()
    hidden_letters = set(hidden_word)
    used_letters = set()


    while len(hidden_letters) > 0:
        guess_so_far = [letter if letter in used_letters else '_' for letter in hidden_word]
        print(f'You have used these letters: ', ' '.join(used_letters))
        print('Current word:', ' '.join(guess_so_far))
        user_guess = input('Guess a letter: ').upper()
        if user_guess not in used_letters:
            used_letters.add(user_guess)
            if user_guess in hidden_letters:
                hidden_letters.remove(user_guess)
        elif user_guess in used_letters:
            print('This letter has already been used. Please choose another one. ')
    
    print(f'You have used these letters: ', ' '.join(used_letters))
    print('Current word:', ' '.join(hidden_word))
    print(f'CONGRATULATIONS, You guessed it! The word is {hidden_word}')

hangman(words)