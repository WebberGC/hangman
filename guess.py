import check
import diagrams
import words


def countOccurrences(word, letterInput, guessedLetters, tries, wordCompletion):
    """This function counts the number of times a letter is in the word and prints it."""
    if not check.checkGuessedLetter(letterInput, guessedLetters):
        occurrence = word.count(letterInput)
        if occurrence > 1:
            print("You guessed it! There are", occurrence, "letter", letterInput + "'s in the word!")
        else:
            print("You guessed it! There is", occurrence, "letter", letterInput, "in the word!")
        guessedLetters.append(letterInput)
    diagrams.displayDiagram(tries)
    words.showWord(wordCompletion)
    print()


def displayGuessedLetters(guessedLetters):
    """This function displays the list of guessed letters."""
    print("\nYou have guessed: ", end="")
    for letter in guessedLetters:
        print(letter + ", ", end="")
    print()


# Makes the guess
def makeGuess(letterInput, word, points, guessedLetters, wordCompletion, tries):
    """This function takes the input, turns it into a guess and displays the appropriate outputs."""
    letterInput = check.checkLetterInput(letterInput)

    # if user guesses the word, their points automatically become enough to win
    if letterInput == word:
        points = len(word)

    # If their guessed letter is in the word print comment and add letter to guessed letters list
    elif letterInput in word:

        # goes through each letter in word, if letter is the same as one in word, it will add it to the list in order
        points += words.charInWord(letterInput, word, wordCompletion, guessedLetters)

        # counts how many times a letter is in the word and prints
        countOccurrences(word, letterInput, guessedLetters, tries, wordCompletion)

        # shows user a list of all the letters already guessed
        displayGuessedLetters(guessedLetters)

    else:
        # Updates tries and displays the appropriate diagram
        tries += 1
        if (7 - tries) != 0:
            diagrams.displayDiagram(tries)

            # Shows the word to the screen
            words.showWord(wordCompletion)
            print()

            print("\nSorry. That letter isn't in the word. You have", (7 - tries), "tries left.")
            guessedLetters.append(letterInput)
            displayGuessedLetters(guessedLetters)

    return points, tries

