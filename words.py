import random
import webScraping

words = []


def charInWord(letterInput, word, wordCompletion, points):
    """This function goes through each letter in the word and checks if it is the same as the letter inputted. If it
    is, it will add it to the wordCompletion list in order."""
    newWordCompletion = []

    for num in range(0, len(wordCompletion)):
        if word[num] == letterInput:
            newWordCompletion.append(word[num] + " ")
            points += 1
        else:
            newWordCompletion.append(wordCompletion[num])
    return newWordCompletion, points


def selectWord():
    """This function picks a random word from the list of words."""
    word = random.choice(words)
    return word


def showWordLength(wordCompletion, word):
    """This function prints the length of the word, creates a list of underscores the same length as the
    word, then it prints the list of underscores."""
    for letter in word:
        if letter.isalpha():
            wordCompletion.append("_ ")
        else:
            wordCompletion.append(letter + " ")
    return wordCompletion


def showWord(wordCompletion):
    """This function prints the wordCompletion list with a space between each letter."""
    displayWord = ""
    for x in wordCompletion:
        displayWord += (x + " ")
    return displayWord


def wordSelection(num):
    webScraping.webScrape(num)
    word = selectWord()

    # Checks how many letters are in the word
    count = 0
    for letter in word:
        if letter.isalpha():
            count += 1
    return word, count
