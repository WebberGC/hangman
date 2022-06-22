import diagrams
import words


def checkInput(userInput):
    """This function checks the user input about playing to see if it is valid."""
    # Goes through the loop while userInput is not y or n
    while userInput.lower() != "y" and userInput.lower() != "n":
        try:
            # Prompts user to see if they wish to play the game
            userInput = input("Do you wish to play? y/n ").lower()

            # Throws an error if response is not y or n
            if userInput != "y" and userInput != "n":
                raise InvalidInput()

        # Displays error message
        except InvalidInput:
            print("Sorry that is not a valid response. Please enter either 'y' or 'n'.\n")
    return userInput


def checkLetterInput(userInput):
    """This function checks the letter to see if it valid."""
    while not userInput.isalpha():
        userInput = input("\nSorry. That was an invalid input. Please guess your first letter: ").lower()
    return userInput


def checkCategory(categoryInput):
    """This function checks the category to see if it is valid."""
    while categoryInput < 1 or categoryInput > len(words.words):
        try:
            # prompts user with categories and asks them to pick one
            print("\n1. Hard words")
            print("2. TV Shows")
            print("3. Countries")
            print("4. Famous Australians")
            categoryInput = int(input("\nPlease select a category by typing the corresponding number: "))

            # Throws an error if the categoryInput is not in the list
            if categoryInput < 1 or categoryInput > len(words.words):
                raise InvalidInput()

        # Displays error message
        except InvalidInput and TypeError:
            categoryInput = input("Invalid userInput. Please select a number between 1 and 4: ")
    return categoryInput


# Checks the condition o
def checkEndCondition(points, word, gameStats, tries):
    """This function checks the end condition at the end of the game. It works out whether the game was finished due
    to no more turns or the word was completed."""
    # if points equal length of word, player wins
    if points == len(word):
        print("\nCongratulations! You won!")

        # Updates and displays the stats to the screen
        gameStats['game'] += 1
        gameStats['win'] += 1
        print("You have won", gameStats['win'], "games and lost", gameStats['loss'], "games. Your win percentage is:",
              str((gameStats['win'] / gameStats['game']) * 100) + "%")

    # if points do not equal length of word, player loses
    else:
        print("\nSorry, you have run out of tries.")
        diagrams.displayDiagram(tries)
        print("\nThe word was: ", word)

        # Updates and displays the stats to the screen
        gameStats['game'] += 1
        gameStats['loss'] += 1
        print("You have won", gameStats['win'], "games and lost", gameStats['loss'], "games. Your win percentage is:",
              str((gameStats['win'] / gameStats['game']) * 100) + "%")
    return gameStats


class InvalidInput(Exception):
    """An exception used when the input in invalid."""
    pass
