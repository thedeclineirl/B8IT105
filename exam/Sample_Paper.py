# Document Analyser
class DocumentAnalyser():
	def __init__(self):
		pass

	def count_lines(self,data):
		return len(data)

	def count_words(self,doc):
		word_count = 0
		for line in data:
			word_count += len(line.split())
		return word_count

	def count_char(self,doc):
		count = 0
		for line in data:
			count += len(line)
		return count

	def average_char_per_line(self,data):
		return self.count_char(data)/self.count_lines(data)

	def average_words_per_line(self,data):
		return self.count_words(data)/self.count_lines(data)

	def average_char_per_word(self,data):
		return self.count_char(data)/self.count_words(data)

analyser = DocumentAnalyser()
data = ['Line one of book','this is the second line','this is the third line']
print(analyser.count_lines(data))
print(analyser.count_words(data))
print(analyser.count_char(data))
print('Average characters per Line: {0}'.format(analyser.average_char_per_line(data)))
print('Average words per Line: {0}'.format(analyser.average_words_per_line(data)))
print('Average characters per Word: {0}'.format(analyser.average_char_per_word(data)))

import unittest
class DocumentAnalyserTest(unittest.TestCase):
	def test_number_of_lines(self):
		analyser = DocumentAnalyser()
		data = ['Line one of book','this is the second line','this is the third line'] 
		self.assertEqual(3,analyser.count_lines(data))

if __name__ == '__main__':
	unittest.main()