import re

class WordsFinder:
    def __init__(self, *file_names):
            self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for files in self.file_names:
            with open(files, encoding='utf-8') as file_:
                for words in file_:
                    words = re.split(r'[,.=!?;:-]+', words.lower())
                    all_words[files] = words
        return all_words

    def find(self, word):
        find_word = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word in words:
                for w in words:
                    if w == word:
                        found_words = w
                        find_word[name] = found_words
        return find_word

    def count(self, word):
        count_word = {}
        word = word.lower()
        count = 0
        for name, words in self.get_all_words().items():
            count = words.count(word)
            if count > 0:
                count_word[name] = count + 1
        return count_word



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего




