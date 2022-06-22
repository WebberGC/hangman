import check
import guess
import words


def run():
	"""This function runs the hangman game"""
	# Initialises userInput, categoryInput and game stats
	userInput = ""
	categoryInput = 0
	gameStats = {"win": 0, "loss": 0, "game": 0}

	# Welcome message
	print("Welcome to Hangman!\n")

	# While userInput is NOT y/n, ask again
	userInput = check.checkInput(userInput)

	while userInput == "y":
		guessedLetters = []  # Initialises guessedLetters (showing all the guessed letters)
		wordCompletion = []  # Initialises wordCompletion (showing how complete the word is)
		tries, points, charIndex = 0, 0, 0  # Initialises tries, points and charIndex as 0

		# Checks the input for category selection
		categoryInput = check.checkCategory(categoryInput)

		# Selects a word from the list of words
		word = words.selectWord(categoryInput)

		# Shows user the length of thr word
		wordCompletion = words.showWordLength(wordCompletion, word)

		# Prompts user to guess their first letter
		letterInput = input("\nPlease guess your first letter: ").lower()
		print()

		# turns letterInput into a guess and displays the appropriate outputs
		points, tries = guess.makeGuess(letterInput, word, points, guessedLetters, wordCompletion, guess, tries)

		# This is the main game loop. It will continue to run until the user has guessed all the letters in the word or
		# has run out of tries.
		while points < len(word) and tries < 7:
			# Prompts user to guess their next letter
			letterInput = input("Please guess your next letter: ").lower()
			print()
			letterInput = check.checkLetterInput(letterInput)

			# turns letterInput into a guess and displays the appropriate outputs
			points, tries = guess.makeGuess(letterInput, word, points, guessedLetters, wordCompletion, guess, tries)

		# Checks the condition of the end game and updates game stats
		gameStats = check.checkEndCondition(points, word, gameStats, tries)

		# Asks if the player wants to play again
		userInput = input("Do you wish to play again? Y/N ").lower()
		userInput = check.checkInput(userInput)

	# If user selects N, the game ends
	print("\nThanks for playing! Goodbye.")
