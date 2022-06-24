import pygame


def setLetterButtonValues(measurements, letters, letterAValue):
	# Goes through every letter and assigns the X and Y coordinates
	for buttonNum in range(26):
		x = measurements["StartX"] + measurements["Gap"] * 2 + ((measurements["Radius"] * 2 + measurements["Gap"]) * (
				buttonNum % 13))
		y = measurements["StartY"] + ((buttonNum // 13) * (measurements["Gap"] + measurements["Radius"] * 2))

		# Adds the x, y, the letter and the visibility to letters
		letters.append([x, y, chr(buttonNum + letterAValue), True])
	return letters


def setCategoryButtons(categories, win, gameDict):
	text = gameDict[2]["LetterFont"].render("Select a category", True, gameDict[1]["Black"])
	textBox = text.get_rect(center=(gameDict[0]["Width"] / 2, gameDict[0]["Height"] / 6))
	win.blit(text, textBox)

	top = 180  # Sets the height of the top button
	for category in categories:
		pygame.draw.rect(win, gameDict[1]["Black"], (270, (top - 15), 250, 35))
		text = gameDict[2]["LetterFont"].render(category, True, gameDict[1]["White"])
		win.blit(text, (400 - text.get_width() / 2, top - text.get_height() / 2))
		top += 50
