import unittest
import check
import words


class Check(unittest.TestCase):
	def test_checkEndCondition_win(self):
		word = "Hello"
		points = 5
		gameStats = {"win": 0, "loss": 0, "game": 0}
		tries = 1
		gameStats = check.checkEndCondition(points, word, gameStats, tries)
		self.assertEqual(gameStats["win"], 1)
		self.assertEqual(gameStats["loss"], 0)
		self.assertEqual(gameStats["game"], 1)

	def test_checkEndCondition_loss(self):
		word = "Hello"
		points = 4
		gameStats = {"win": 0, "loss": 0, "game": 0}
		tries = 7
		gameStats = check.checkEndCondition(points, word, gameStats, tries)
		self.assertEqual(gameStats["win"], 0)
		self.assertEqual(gameStats["loss"], 1)
		self.assertEqual(gameStats["game"], 1)


class Words(unittest.TestCase):
	def test_charInWord_one(self):
		letterInput = "e"
		word = "hello"
		wordCompletion = ["_", "_", "_", "_", "_"]
		point = words.charInWord(letterInput, word, wordCompletion)
		self.assertEqual(point, 1)

	def test_charInWord_two(self):
		letterInput = "l"
		word = "hello"
		wordCompletion = ["_", "_", "_", "_", "_"]
		point = words.charInWord(letterInput, word, wordCompletion)
		self.assertEqual(point, 2)

	def test_charInWord_none(self):
		letterInput = "z"
		word = "hello"
		wordCompletion = ["_", "_", "_", "_", "_"]
		point = words.charInWord(letterInput, word, wordCompletion)
		self.assertEqual(point, 0)

unittest.main()