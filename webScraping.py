import requests
from bs4 import BeautifulSoup
import words


def webScrape(selection):
	categories = [None, hardWords, tvShows, countries, famousAustralians, aflPlayers]
	categories[selection]()


def hardWords():
	# Hard words
	connection = getResponse('https://www.hangmanwords.com/words')
	results = connection.find('ul', class_="Words_wordlist__i4vT0")
	for li in results.findAll('li'):
		words.words.append(li.text.strip())


def tvShows():
	# TV Shows
	connection = getResponse('https://www.imdb.com/chart/toptv/')
	results = connection.find('tbody', class_="lister-list")
	for tr in results.findAll('tr'):
		titleColumn = tr.find('td', class_="titleColumn")
		for show in titleColumn.find('a'):
			if not show.isnumeric():
				words.words.append(show.text.strip().lower())


def countries():
	connection = getResponse('https://www.worldometers.info/geography/alphabetical-list-of-countries/')
	results = connection.find('tbody')
	td = results.findAll('td')
	for country in td:
		if country.text.strip().isalpha():
			words.words.append(country.text.strip().lower())


def famousAustralians():
	# Famous Australian's
	connection = getResponse('https://www.thefamouspeople.com/australia.php')
	wrapper = connection.findAll(class_="wrapper")
	for celebrity in wrapper:
		title = celebrity.find(class_="tileLink")
		if title is not None:
			words.words.append(title.text.strip().lower())


def aflPlayers():
	# AFL Players
	connection = getResponse('https://www.footywire.com/afl/footy/ft_players')
	results = connection.findAll(class_="lnormtop")
	for lnormtop in results:
		playerLink = lnormtop.findAll('a')
		for player in playerLink:
			if player is not None:
				playerNameList = player.text.strip().split(", ")
				playerName = playerNameList[1] + " " + playerNameList[0]
				words.words.append(playerName.lower())


def getResponse(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content, "html.parser")
	return soup
