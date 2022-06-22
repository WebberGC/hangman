import random

words = \
    [["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon",
      "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful",
      "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness",
      "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves",
      "embezzle", "equip", "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack",
      "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby", "galaxy",
      "galvanize", "gazebo", "giaour", "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess",
      "haiku", "haphazard", "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice",
      "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging",
      "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte",
      "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis",
      "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub", "nowadays", "numbskull",
      "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia",
      "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", "quiz", "quizzes",
      "quorum", "razzmatazz", "rhubarb", "rhythm", "rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx",
      "spritz", "squawk", "staff", "strength", "strengths", "stretch", "stronghold", "stymied", "subway", "swivel",
      "syndrome", "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant", "triphthong",
      "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo",
      "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing",
      "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee",
      "yoked", "youthful", "yummy", "zephyr", "zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie"],
     ["brooklynninenine", "theoffice", "rickandmorty", "greysanatomy", "gameofthrones", "supernatural", "doctorwho",
      "gameofthrones", "friends", "breakingbad", "thegoodplace", "thewalkingdead", "newamsterdam", "thegooddoctor",
      "westworld", "criminalminds", "thevampirediaries", "howimetyourmother", "thesimpsons", "futurama", "familyguy",
      "bones", "therookie", "wentworth", "dexter", "pokemon", "gossipgirl", "house", "houseofcards", "lost", "lucifer",
      "ncis", "prisonbreak", "scrubs", "sherlock", "suits", "thexfiles", "buffythevampireslayer", "seinfeld",
      "parksandrecreation", "americanhorrorstory", "modernfamily", "arresteddevelopment", "shameless", "offspring",
      "blackmirror", "thecrown"],
     ["afghanistan", "albania", "algeria", "andorra", "angola", "antiguaandbarbuda", "argentina", "armenia",
      "australia", "austria", "azerbaijan", "bahrain", "bangladesh", "barbados", "belarus", "belgium", "belize",
      "benin", "bhutan", "bolivia", "bosniaandherzegovina", "botswana", "brazil", "brunei", "bulgaria", "burkinafaso",
      "burundi", "caboverde", "cambodia", "cameroon", "canada", "centralafricanrepublic", "chad", "chile", "china",
      "colombia", "comoros", "congo", "costarica", "croatia", "cuba", "cyprus", "czechrepublic", "denmark", "djibouti",
      "dominica", "dominicanrepublic", "easttimor", "ecuador", "egypt", "elsalvador", "equatorialguinea", "eritrea",
      "estonia", "eswatini", "ethiopia", "fiji", "finland", "france", "gabon", "georgia", "germany", "ghana", "greece",
      "grenada", "guatemala", "guinea", "guineabissau", "guyana", "haiti", "honduras", "hungary", "iceland", "india",
      "indonesia", "iran", "iraq", "ireland", "israel", "italy", "jamaica", "japan", "jordan", "kazakhstan", "kenya",
      "kiribati", "kosovo", "kuwait", "kyrgyzstan", "laos", "latvia", "lebanon", "lesotho", "liberia", "libya",
      "liechtenstein", "lithuania", "luxembourg", "madagascar", "malawi", "malaysia", "maldives", "mali", "malta",
      "mauritania", "mauritius", "mexico", "moldova", "monaco", "mongolia", "montenegro", "morocco", "mozambique",
      "namibia", "nauru", "nepal", "netherlands", "newzealand", "nicaragua", "niger", "nigeria", "northkorea",
      "northmacedonia", "norway", "oman", "pakistan", "palau", "panama", "papuanewguinea", "paraguay", "peru",
      "philippines", "poland", "portugal", "qatar", "romania", "russia", "rwanda", "saintkittsandnevis", "saintlucia",
      "samoa", "sanmarino", "saudiarabia", "senegal", "serbia", "seychelles", "sierraleone", "singapore", "slovakia",
      "slovenia", "solomonislands", "somalia", "southafrica", "southkorea", "spain", "srilanka", "sudan", "sudan",
      "suriname", "sweden", "switzerland", "syria", "taiwan", "tajikistan", "tanzania", "thailand", "thebahamas",
      "thegambia", "togo", "tonga", "trinidadandtobago", "tunisia", "turkey", "turkmenistan", "tuvalu", "uganda",
      "ukraine", "unitedarabemirates", "unitedkingdom", "unitedstates", "uruguay", "uzbekistan", "vanuatu",
      "vaticancity", "venezuela", "vietnam", "yemen", "zambia", "zimbabwe"],
     ["nicolekidman", "melgibson", "russellcrowe", "olivianewtonjohn", "heathledger", "paulhogan", "cateblanchett",
      "hughjackman", "kylieminogue", "chrishemsworth", "liamhemsworth", "margotrobbie", "mirandakerr", "keithurban",
      "islafisher", "hugoweaving", "rebelwilson", "steveirwin", "angusyoung", "rubyrose", "iggyazalea", "bensimmons",
      "sirdonaldbradman", "ericbana", "nedkelly", "elizataylor", "portiaderossi", "robertiwin", "bindiirwin",
      "deltagoodrem", "nickkyrgios", "claireholt", "rickspringfield", "scottmorrison", "codysimpson", "ashleighbarty",
      "juliagillard", "tonyabbott", "davidwarner", "bazluhrmann"]]


def charInWord(letterInput, word, wordCompletion):
    """This function goes through each letter in the word and checks if it is the same as the letter inputted. If it
    is, it will add it to the wordCompletion list in order."""
    charIndex = 0
    point = 0
    for letter in word:
        if letterInput == letter:
            point += 1
            wordCompletion[charIndex] = letter
        charIndex += 1
    return point


def selectWord(categoryInput):
    """This function picks a random word from the list of words."""
    word = random.randint(1, len(words[int(categoryInput) - 1]))  # Gives a random number within a category
    word = words[int(categoryInput) - 1][word - 1]  # picks a word in the category
    return word


def showWordLength(wordCompletion, word):
    """This function prints the length of the word, creates a list of underscores the same length as the
    word, then it prints the list of underscores."""
    print("\nGreat. Your word has", len(word), "letters")
    wordCompletion = ["_"] * len(word)
    print()
    showWord(wordCompletion)
    return wordCompletion


def showWord(wordCompletion):
    """This function prints the wordCompletion list with a space between each letter."""
    for x in wordCompletion:
        print(x, end=" ")
