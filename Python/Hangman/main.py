from wordArray import hangman_words
import random

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]

def play_hangman():
    word = random.choice(hangman_words)
    word_letters = set(word)  # letters in the word
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()  # what the user has guessed

    tries = 6  # number of tries

    # getting user input
    while len(word_letters) > 0 and tries > 0:
        print("You have", tries, "tries left.")
        print("Used letters:", ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print(display_hangman(tries))
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                tries = tries - 1
                print("Letter is not in the word.")
        
        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.")
        
        else:
            print("Invalid character. Please try again.")

    # gets here when len(word_letters) == 0 OR when tries == 0
    if tries == 0:
        print(display_hangman(tries))
        print("Sorry, you died. The word was", word)
    else:
        print("Congratulations! You guessed the word", word, "!!")

play_hangman()