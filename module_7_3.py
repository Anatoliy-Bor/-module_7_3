
class WordsFinder:
	def __init__(self, file_names):
		self.file_names = file_names
	def get_all_words(self):
		all_words = {}
		with open(self.file_names, 'r', encoding='utf-8') as file:
			words = []
			for i in file:
				lower_case = i.lower()
				punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
				for punct in punctuation:
					lower_case = lower_case.replace(punct, '')
				words.extend(lower_case.split())
			all_words[self.file_names] = words
		return all_words

	def find(self, word):
		places = {}
		for key, value in self.get_all_words().items():
			if word.lower() in value:
				places[key] = value.index(word.lower()) + 1
		return places

	def count(self, word):
		counters = {}
		for value, key in self.get_all_words().items():
			words_count = key.count(word.lower())
			counters[value] = words_count
		return counters

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
