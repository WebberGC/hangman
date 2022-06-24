import pygame


def setUpScreen(measurements):
	# Setup display
	win = pygame.display.set_mode((measurements["Width"], measurements["Height"]))
	pygame.display.set_caption("Hangman Game!")
	return win


def loadImages():
	images = []
	for num in range(7):
		image = pygame.image.load("Images/hangman" + str(num) + ".png")
		images.append(image)
	return images


def setUpPygameClock():
	FPS = 60
	clock = pygame.time.Clock()
	game = True
	return FPS, clock, game
