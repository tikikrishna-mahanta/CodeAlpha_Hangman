import random


def display_word(secret_word, guessed_letters):
    word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            word += letter + " "
        else:
            word += "_ "

    return word.strip()


def play_game():
    words = ["python", "computer", "programming", "keyboard", "internet"]

    secret_word = random.choice(words)
    guessed_letters = []

    max_wrong_guesses = 6
    wrong_guesses = 0

    print("=" * 35)
    print("          HANGMAN GAME")
    print("=" * 35)
    print("Try to guess the word one letter at a time.")
    print("You can make up to 6 wrong guesses.\n")

    while wrong_guesses < max_wrong_guesses:

        print("Word:", display_word(secret_word, guessed_letters))
        print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

        if guessed_letters:
            print("Guessed letters:", ", ".join(guessed_letters))
        else:
            print("Guessed letters: None")

        if all(letter in guessed_letters for letter in secret_word):
            print("\nYou got it! The word was:", secret_word)
            print("Congratulations! You won!")
            return

        guess = input("\nGuess a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1:
            print("Invalid input. Please enter exactly one letter.\n")
            continue

        if not ("a" <= guess <= "z"):
            print("Invalid input. Please enter a letter from A to Z.\n")
            continue

        # Check for repeated guesses
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.\n")
            continue

        guessed_letters.append(guess)

        # Check the guess
        if guess in secret_word:
            print("Nice! That letter is in the word.\n")
        else:
            wrong_guesses += 1
            print("That letter is not in the word.\n")

    print("You've used all 6 wrong guesses.")
    print("Game over!")
    print("The word was:", secret_word)


print("Welcome!")
play_game()
print("\nThanks for playing!")