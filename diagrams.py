# List of diagrams to use when user gets a letter wrong
diagrams = \
	["   +---+\n       |\n       |\n       |\n      ===",
	 "   +---+\n   o   |\n       |\n       |\n      ===",
	 "   +---+\n   o   |\n   |   |\n       |\n      ===",
	 "   +---+\n   o   |\n  /|   |\n       |\n      ===",
	 "   +---+\n   o   |\n  /|\  |\n       |\n      ===",
	 "   +---+\n   o   |\n  /|\  |\n  /    |\n      ===",
	 "   +---+\n   o   |\n  /|\  |\n  / \  |\n      ==="]


# Printing the diagram that corresponds to the number of tries the user has left.
def displayDiagram(tries):
	"""This function prints the diagram that corresponds to the number of tries the user has left."""
	if tries != 0:
		print(diagrams[tries - 1])
