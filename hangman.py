import setItem
import words
import pygame
import gui
import math


def run():
	"""This function runs the hangman game"""
	# Initialises pygame
	pygame.init()

	# Sets all the measurements, game stats, colours, fonts and categories in the game within a dictionary
	measurements = {"Radius": 20, "Gap": 15, "StartY": 400, "Height": 500, "Width": 800}
	gameStats = {"win": 0, "loss": 0, "game": 0}
	colours = {"White": (255, 255, 255), "Black": (0, 0, 0)}
	fonts = {"LetterFont": pygame.font.SysFont('comicsans', 25), "WordFont": pygame.font.SysFont('arial', 25)}
	categories = ["Hard Words", "TV Shows", "Countries", "Famous Australians", "AFL Players"]
	gameDicts = [measurements, colours, fonts]

	# Initialises the game variables
	word = None
	setup = True
	gameStatsSet = False
	count = 0
	tries = 0
	points = 0
	wordCompletion = []
	letters = []

	# Sets up the clock, screen and images within the game
	win = gui.setUpScreen(measurements)
	images = gui.loadImages()
	FPS, clock, game = gui.setUpPygameClock()

	# The X position of the left-most button
	measurements["StartX"] = round(
		(measurements["Width"] - (measurements["Radius"] * 2 + measurements["Gap"]) * 13) / 2)

	# Goes through every letter, assigns the X and Y coordinates and adds them to the letters list
	letters = setItem.setLetterButtonValues(measurements, letters, 65)

	while game:
		# Sets how fast the game goes
		clock.tick(FPS)

		# Sets the screen to white
		win.fill(colours["White"])

		while setup:
			gameStatsSet = False  # Prevents wins/losses/game from being added multiple times a game

			# Creates all the category buttons
			setItem.setCategoryButtons(categories, win, gameDicts)

			# Updates the screen
			pygame.display.update()

			# What occurs every time something is clicked
			for event in pygame.event.get():

				# Quits the game if the X button is pressed
				if event.type == pygame.QUIT:
					game = False
					setup = False

				# Gets the position of the mouse on click
				if event.type == pygame.MOUSEBUTTONDOWN:
					mouseX, mouseY = pygame.mouse.get_pos()

					# Hard Words
					if (270 < mouseX < 520) and (165 < mouseY < 200):
						word, count = words.wordSelection(1)
						setup = False

					# TV Shows
					elif (270 < mouseX < 520) and (215 < mouseY < 250):
						word, count = words.wordSelection(2)
						setup = False

					# Countries
					elif (270 < mouseX < 520) and (265 < mouseY < 300):
						word, count = words.wordSelection(3)
						setup = False

					# Famous Australians
					elif (270 < mouseX < 520) and (315 < mouseY < 350):
						word, count = words.wordSelection(4)
						setup = False

					# AFL Players
					elif (270 < mouseX < 520) and (365 < mouseY < 400):
						word, count = words.wordSelection(5)
						setup = False

		# Loops through while the game is playing
		while points < count and tries < 7:

			# Sets the screen to white
			win.fill(colours["White"])

			if not wordCompletion:
				# Shows user the length of thr word
				wordCompletion = words.showWordLength(wordCompletion, word)

			# Create the text that is displayed on the screen
			displayWord = words.showWord(wordCompletion)

			# Displays the word
			text = fonts["WordFont"].render(displayWord, True, colours["Black"])
			win.blit(text, (400, 200))

			# Goes through every letter and sets the letter and it's coordinates
			for letter in letters:
				x, y, ltr, visible = letter

				# If the button is visible, create the letter button
				if visible:
					pygame.draw.circle(win, colours["Black"], (x, y), measurements["Radius"], 3)
					text = fonts["LetterFont"].render(ltr, True, colours["Black"])
					win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

			# Set the hangman image
			win.blit(images[tries], (150, 100))
			pygame.display.update()

			# What occurs every time something is clicked
			for event in pygame.event.get():

				# Sets tries and points as 100 to exit the loop
				if event.type == pygame.QUIT:
					tries = 100
					points = 100

				# Gets the position of the mouse on click
				if event.type == pygame.MOUSEBUTTONDOWN:
					mouseX, mouseY = pygame.mouse.get_pos()

					# Cycles through each letter
					for letter in letters:
						x, y, ltr, visible = letter

						# checks whether the button was clicked if it was visible
						if visible:
							dis = math.sqrt((x - mouseX) ** 2 + (y - mouseY) ** 2)

							# Turns the button invisible if clicked
							if dis < measurements["Radius"]:
								letter[3] = False
								wordCompletion, points = words.charInWord(ltr.lower(), word, wordCompletion, points)
								# Adds a try if letter is not in the word
								if letter[2].lower() not in word:
									tries += 1
		# Quits the game
		if tries == 100:
			pygame.quit()

		# Shows the appropriate display when player runs out of turns
		elif tries == 7:
			text = fonts["LetterFont"].render("Sorry. The word was " + word, True, colours["Black"])
			textBox = text.get_rect(center=(measurements["Width"] / 2, measurements["Height"] / 6))
			win.blit(text, textBox)

			# Sets the game stats
			if not gameStatsSet:
				gameStats['game'] += 1
				gameStats['loss'] += 1
				gameStatsSet = True

		# Shows the appropriate display when the player guesses the word
		else:
			text = fonts["LetterFont"].render("Congratulations! " + word + " was the word!", True, colours["Black"])
			textBox = text.get_rect(center=(measurements["Width"] / 2, measurements["Height"] / 6))
			win.blit(text, textBox)

			# Sets the game stats
			if not gameStatsSet:
				gameStats['game'] += 1
				gameStats['win'] += 1
				gameStatsSet = True

		# Displays the "Do you want to play again?" message
		text = fonts["LetterFont"].render("Do you want to play again?", True, colours["Black"])
		win.blit(text, (250, 140))

		# Displays the text boxes for Yes and No
		pygame.draw.rect(win, colours["Black"], (440, 200, 100, 35))
		pygame.draw.rect(win, colours["Black"], (270, 200, 100, 35))

		# Displays the Yes text
		text = fonts["LetterFont"].render("Yes", True, colours["White"])
		win.blit(text, (300, 197))

		# Displays teh No text
		text = fonts["LetterFont"].render("No", True, colours["White"])
		win.blit(text, (475, 197))

		# Updates the screen
		pygame.display.update()

		# What occurs every time something is clicked
		for event in pygame.event.get():

			# Quits the game if the X button is pressed
			if event.type == pygame.QUIT:
				game = False

			# Gets the position of the mouse on click
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouseX, mouseY = pygame.mouse.get_pos()

				# Play Again
				if (270 < mouseX < 370) and (200 < mouseY < 230):
					# Resets all the values
					setup = True
					points = 0
					count = 0
					word = ""
					wordCompletion = []
					tries = 0

					# Resets all the letters
					for letter in letters:
						letter[3] = True

				# Quit
				elif (440 < mouseX < 540) and (200 < mouseY < 230):
					game = False

	# Quits the program
	pygame.quit()
