# CodeAlpha Hangman 

A simple Hangman game built with Python as part of my CodeAlpha Python Programming Internship.

## About the Project

I built this project to practice the basics of Python by creating a small game that runs directly in the terminal.

The computer randomly picks a word from a list, and the player has to guess it one letter at a time. The player gets a maximum of 6 wrong guesses before the game ends.

## What the Game Can Do

- Randomly selects a word from 5 predefined words
- Lets the player guess one letter at a time
- Shows the letters that have been guessed correctly
- Allows a maximum of 6 wrong guesses
- Detects repeated guesses
- Checks invalid inputs
- Handles words with repeated letters
- Shows whether the player won or lost

## Words Used

The current word list contains:

- Python
- Computer
- Programming
- Keyboard
- Internet

## Built With

- Python 3
- `random`
- Functions
- Lists
- Strings
- `while` loops
- `if-else` conditions
- User input and console output

## How to Run

Make sure Python 3 is installed.

Open the terminal in this project folder and run:

```bash
python hangman.py




        Example:

===================================
          HANGMAN GAME
===================================

Word: _ _ _ _ _ _
Wrong guesses: 0 / 6

Guess a letter: p
Nice! That letter is in the word.