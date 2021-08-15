# imports random for random word
import random

# List of words used in the hangman game
words = \
[["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon",
  "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo",
  "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness", "croquet",
  "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves", "embezzle", "equip",
  "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness",
  "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour",
  "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard", "hyphen",
  "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest",
  "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful", "juicy",
  "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz",
  "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave",
  "mnemonic", "mystify", "naphtha", "nightclub", "nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize",
  "oxygen", "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy",
  "puzzling", "quartz", "queue", "quips", "quixotic", "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm",
  "rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths",
  "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz",
  "transcript", "transgress", "transplant", "triphthong", "twelfth", "twelfths", "unknown", "unworthy", "unzip",
  "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy",
  "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy",
  "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag",
  "zigzagging", "zilch", "zipper", "zodiac", "zombie"],
 ["brooklynninenine", "theoffice", "rickandmorty", "greysanatomy", "gameofthrones", "supernatural", "doctorwho",
  "gameofthrones", "friends", "breakingbad", "thegoodplace", "thewalkingdead", "newamsterdam", "thegooddoctor",
  "westworld", "criminalminds", "thevampirediaries", "howimetyourmother", "thesimpsons", "futurama", "familyguy",
  "bones", "therookie", "wentworth", "dexter", "pokemon", "gossipgirl", "house", "houseofcards", "lost", "lucifer",
  "ncis", "prisonbreak", "scrubs", "sherlock", "suits", "thexfiles", "buffythevampireslayer", "seinfeld",
  "parksandrecreation", "americanhorrorstory", "modernfamily", "arresteddevelopment", "shameless", "offspring",
  "blackmirror", "thecrown"],
 ["afghanistan", "albania", "algeria", "andorra", "angola", "antiguaandbarbuda", "argentina", "armenia", "australia",
   "austria", "azerbaijan", "bahrain", "bangladesh", "barbados", "belarus", "belgium", "belize", "benin", "bhutan",
  "bolivia", "bosniaandherzegovina", "botswana", "brazil", "brunei", "bulgaria", "burkinafaso", "burundi", "caboverde",
  "cambodia", "cameroon", "canada", "centralafricanrepublic", "chad", "chile", "china", "colombia", "comoros", "congo",
  "costarica", "croatia", "cuba", "cyprus", "czechrepublic", "denmark", "djibouti", "dominica", "dominicanrepublic",
  "easttimor", "ecuador", "egypt", "elsalvador", "equatorialguinea", "eritrea", "estonia", "eswatini", "ethiopia",
  "fiji", "finland", "france", "gabon", "georgia", "germany", "ghana", "greece", "grenada", "guatemala", "guinea",
  "guineabissau", "guyana", "haiti", "honduras", "hungary", "iceland", "india", "indonesia", "iran", "iraq", "ireland",
  "israel", "italy", "jamaica", "japan", "jordan", "kazakhstan", "kenya", "kiribati", "kosovo", "kuwait", "kyrgyzstan",
  "laos", "latvia", "lebanon", "lesotho", "liberia", "libya", "liechtenstein", "lithuania", "luxembourg", "madagascar",
  "malawi", "malaysia", "maldives", "mali", "malta", "mauritania", "mauritius", "mexico", "moldova", "monaco",
  "mongolia", "montenegro", "morocco", "mozambique", "namibia", "nauru", "nepal", "netherlands", "newzealand",
  "nicaragua", "niger", "nigeria", "northkorea", "northmacedonia", "norway", "oman", "pakistan", "palau", "panama",
  "papuanewguinea", "paraguay", "peru", "philippines", "poland", "portugal", "qatar", "romania", "russia", "rwanda",
  "saintkittsandnevis", "saintlucia", "samoa", "sanmarino", "saudiarabia", "senegal", "serbia", "seychelles",
  "sierraleone", "singapore", "slovakia", "slovenia", "solomonislands", "somalia", "southafrica", "southkorea",
  "spain", "srilanka", "sudan", "sudan", "suriname", "sweden", "switzerland", "syria", "taiwan", "tajikistan",
  "tanzania", "thailand", "thebahamas", "thegambia", "togo", "tonga", "trinidadandtobago", "tunisia", "turkey",
  "turkmenistan", "tuvalu", "uganda", "ukraine", "unitedarabemirates", "unitedkingdom", "unitedstates", "uruguay",
  "uzbekistan", "vanuatu", "vaticancity", "venezuela", "vietnam", "yemen", "zambia", "zimbabwe"],
 ["helo", "light", "tesing", "pencil"]]

# List of diagrams to use when user gets a letter wrong
diagrams = \
    ["   +---+\n       |\n       |\n       |\n      ===",
     "   +---+\n   o   |\n       |\n       |\n      ===",
     "   +---+\n   o   |\n   |   |\n       |\n      ===",
     "   +---+\n   o   |\n  /|   |\n       |\n      ===",
     "   +---+\n   o   |\n  /|\  |\n       |\n      ===",
     "   +---+\n   o   |\n  /|\  |\n  /    |\n      ===",
     "   +---+\n   o   |\n  /|\  |\n  / \  |\n      ==="]

# List of guessed letters
guessedLetters = []

# What is printed out to user when they guess
wordCompletion = []

win = 0
loss = 0
game = 0

# User input asking the user if they wish to play
playInput = input("Welcome to Hangman! Do you wish to play? Y ").lower()

# While user has selected Y, the game will commence
while playInput == "y":

    # prompts user with categories and asks them to pick one
    print("\n1. Hard words")
    print("2. TV Shows")
    print("3. Countries")
    categoryInput = int(input("\nPlease select a category by typing the corresponding number: "))

    # random number is selected which picks a word from the words list
    word = random.randint(1, len(words[categoryInput - 1]))     # Gives a random number within a category
    word = words[categoryInput-1][word-1]                       # picks a word in the category
    tries = 0
    points = 0
    charIndex = -1

    # Shows user how many letters are in the randomised word
    print("\nGreat. Your word has", len(word), "letters")
    wordCompletion = ["_"] * len(word)
    print(wordCompletion)

    # Prompts user to guess their first letter
    letterInput = input("\nPlease guess your first letter: ").lower()

    # while user input is not a letter, it will prompt user to try again
    while not letterInput.isalpha():
        letterInput = input("\nSorry. That was an invalid input. Please guess your first letter: ").lower()

    # if user guesses the word, their points automatically become enough to win
    if letterInput == word:
        points = len(word)

    # If their guessed letter is in the word print comment and add letter to guessed letters list
    elif letterInput in word:

        # counts how many times a letter is in the word and prints
        occurrence = word.count(letterInput)
        if occurrence > 1:
            print("You guessed it! There are",occurrence,"letter",letterInput+"'s in the word!")
        else:
            print("You guessed it! There is",occurrence,"letter",letterInput,"in the word!")
        guessedLetters.append(letterInput)

        # goes through each letter in word, if letter is the same as one in char, it will add it to the list in order
        for char in word:
            charIndex += 1
            if letterInput == char:
                points += 1
                wordCompletion[charIndex] = char

        # Resets charIndex back to -1
        charIndex = -1

        # Prints the list with all the correct guesses
        print(wordCompletion)

        # shows user a list of all the letters already guessed
        print("\nYou have already guessed:", guessedLetters)

    # If their guessed letter was not in the word, print comment and add 1 to tries
    else:
        tries += 1
        print("Sorry. That letter isn't in the word. You have",(7-tries),"tries left.")
        print(diagrams[tries-1])
        print(wordCompletion)
        guessedLetters.append(letterInput)
        print("\nYou have already guessed:",guessedLetters)

    # while points do not equal the length of the random word AND tries are less than 7, game continues
    while points != len(word) and tries < 7:

        # Prompts user to guess their next letter
        letterInput = input("\nPlease guess your next letter: ").lower()

        # while user input is not a letter, it will prompt user to try again
        while not letterInput.isalpha():
            letterInput = input("\nSorry. That was an invalid input. Please guess your first letter: ").lower()

        while letterInput in guessedLetters:
            letterInput = input("\nYou have already guessed that letter, please try again: ").lower()

            # while user input is not a letter, it will prompt user to try again
            while not letterInput.isalpha():
                letterInput = input("\nSorry. That was an invalid input. Please guess your first letter: ").lower()

        # if user guesses the word, their points automatically become enough to win
        if letterInput == word:
            points = len(word)

        # If their guessed letter is in the word print comment and add letter to guessed letters list
        elif letterInput in word:
            occurrence = word.count(letterInput)
            if occurrence > 1:
                print("\nYou guessed it! There are", occurrence, "letter", letterInput + "'s in the word!")
                print("You have",(7-tries),"tries left.")
            else:
                print("\nYou guessed it! There is", occurrence, "letter", letterInput, "in the word!")
                print("You have", (7 - tries), "tries left.")
            guessedLetters.append(letterInput)

            # goes through each letter in word, if letter is the same as one in char it will add it to the list in order
            for char in word:
                charIndex += 1
                if letterInput == char:
                    points += 1
                    wordCompletion[charIndex] = char

            # Resets charIndex back to -1
            charIndex = -1

            # if tries do not equal 0, print the hangman diagram
            if tries != 0:
                print(diagrams[tries-1])

            # prints the list with all the correct guesses
            print(wordCompletion)

            # shows user a list of all the letters already guessed
            if points != len(word):
                print("\nYou have already guessed:", guessedLetters)

        # If their guessed letter was not in the word, print comment and add 1 to tries
        else:
            tries += 1

            # if user has 1 try left, it will print 1 try instead of 1 tries
            if (7-tries) == 1:
                print("Sorry. That letter isn't in the word. You have 1 try left.")
            else:
                print("\nSorry. That letter isn't in the word. You have",(7-tries),"tries left.")

            # prints diagram and adds letters to guessed letters and word completion
            print(diagrams[tries - 1])
            print(wordCompletion)
            guessedLetters.append(letterInput)
            print("\nYou have already guessed:", guessedLetters)

    # if points equal length of word, player wins
    if points == len(word):
        print("\nCongratulations! You won!")
        game += 1
        win += 1
        print("You have won",win,"games and lost",loss,"games. Your win percentage is:",str((win/game)*100)+"%")

    # if pints do not equal length of word, player loses
    else:
        print("\nSorry, you have run out of tries.")
        print(diagrams[tries - 1])
        print("\nThe word was: ",word)
        game += 1
        loss += 1
        print("You have won", win, "games and lost", loss, "games. Your win percentage is:",str((win/game)*100)+"%")

    # resetting everything to 0
    guessedLetters = []
    wordCompletion = []

    # The game is finished, prompt to ask whether user wants to play again
    playInput = input("Do you wish to play again? Y/N ").lower()

# If user selects N, the game ends
print("Thanks for playing! Goodbye.")
