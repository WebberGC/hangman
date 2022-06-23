import random
import requests
from bs4 import BeautifulSoup

words = []


def webScrape():
    listCount = 0

    print("\nCollecting words...\n")

    # Hard words
    words.append([])
    connection = getResponse('https://www.hangmanwords.com/words')
    results = connection.find('ul', class_="Words_wordlist__i4vT0")
    for li in results.findAll('li'):
        words[listCount].append(li.text.strip())

    listCount += 1

    # TV Shows
    words.append([])
    connection = getResponse('https://www.imdb.com/chart/toptv/')
    results = connection.find('tbody', class_="lister-list")
    for tr in results.findAll('tr'):
        titleColumn = tr.find('td', class_="titleColumn")
        for show in titleColumn.find('a'):
           words[listCount].append(show.text.strip().lower())
    listCount += 1
    # Countries
   words.append([])
   connection = getResponse('https://www.worldometers.info/geography/alphabetical-list-of-countries/')
   results = connection.find('tbody')
   td = results.findAll('td')
   for country in td:
       if country.text.strip().isalpha():
           words[listCount].append(country.text.strip().lower())
    listCount += 1
    # Famous Australian's
   words.append([])
   connection = getResponse('https://www.thefamouspeople.com/australia.php')
   wrapper = connection.findAll(class_="wrapper")
   for celebrity in wrapper:
       title = celebrity.find(class_="tileLink")
       if title is not None:
           words[listCount].append(title.text.strip().lower())
    listCount += 1
    # AFL Players
   words.append([])
   connection = getResponse('https://www.footywire.com/afl/footy/ft_players')
   results = connection.findAll(class_="lnormtop")
   for lnormtop in results:
       playerLink = lnormtop.findAll('a')
       for player in playerLink:
           if player is not None:
               playerNameList = player.text.strip().split(", ")
               playerName = playerNameList[1] + " " + playerNameList[0]
               words[listCount].append(playerName.lower())
    listCount += 1


ef getResponse(url):
   response = requests.get(url)
   soup = BeautifulSoup(response.content, "html.parser")
   return soup

ef charInWord(letterInput, word, wordCompletion, guessedLetters):
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

ef selectWord(categoryInput):
   """This function picks a random word from the list of words."""
   word = random.randint(1, len(words[int(categoryInput) - 1]))  # Gives a random number within a category
   word = words[int(categoryInput) - 1][word - 1]  # picks a word in the category
   return word

ef showWordLength(wordCompletion, word):
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

ef showWord(wordCompletion):
   """This function prints the wordCompletion list with a space between each letter."""
   for x in wordCompletion:
       print(x, end=" ")

