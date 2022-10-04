import random 
from random-words import words

def hangman(words):
    hidden_word = random.choice(words)
    while '-' in word or ' ' in word:
        hidden_word = random.choice(words)
    
    hidden_letters = set(hidden_word)
    used_letters = set()
    user_guess = input('Guess a letter: ').upper()

    if user_guess not in used_letters:
        used_letters.add(user_guess)
        if user_guess in hidden_letters:
            hidden_letters.remove(user_guess)


