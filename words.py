import random

words = []


def charInWord(letterInput, word, wordCompletion, guessedLetters):
    """This function goes through each letter in the word and checks if it is the same as the letter inputted. If it
    is, it will add it to the wordCompletion list in order."""
    charIndex = 0
    point = 0
    if letterInput not in guessedLetters:
        for letter in word:
            if letterInput == letter:
                point += 1
                wordCompletion[charIndex] = letter
            charIndex += 1
    return point


def selectWord():
    """This function picks a random word from the list of words."""
    word = words[random.randint(1, (len(words) - 1))]
    return word


def showWordLength(wordCompletion, word):
    """This function prints the length of the word, creates a list of underscores the same length as the
    word, then it prints the list of underscores."""
    count = 0

    for letter in word:
        if letter.isalpha():
            count += 1
            wordCompletion.append("_")
        else:
            wordCompletion.append(letter)

    print("\nGreat. Your word has", count, "letters\n")
    showWord(wordCompletion)
    return wordCompletion


def showWord(wordCompletion):
    """This function prints the wordCompletion list with a space between each letter."""
    for x in wordCompletion:
        print(x, end=" ")
