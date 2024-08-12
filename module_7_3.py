class WordsFinder:
    def __init__(self, *files):
        self.file_names = [file_name for file_name in files]

    def get_all_words(self):
        all_words = {}
        symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            words = []
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    for char in line:
                        if char in symbols:
                            line = line.replace(char, '')
                    words += line.lower().split()
            all_words.update({file_name: words})
        return all_words

    def find(self, word):
        find_count = {}
        for keys, value in self.get_all_words().items():
            if word.lower() in value:
                find_count.update({keys: value.index(word.lower()) + 1})
            else:
                find_count.update({keys: f'Слова {word} в файле нет'})
        return find_count

    def count(self, word):
        count_dict = {}
        for keys, values in self.get_all_words().items():
            count = 0
            for value in values:
                if word.lower() in value:
                    count += 1
            count_dict.update({keys: count})
        return count_dict


finder2 = WordsFinder('test_file.txt', 'test_file_2.txt')
print(finder2.get_all_words())
print(finder2.find('text'))
print(finder2.count('if'))
