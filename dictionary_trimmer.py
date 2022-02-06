""" Helper to drop unnecessary words from word dictionary file. """
EN_FILENAME = 'app/static/words.txt'  # Scrabble (for now) EN word list
with open(EN_FILENAME, encoding='utf-8') as en_file:
    EN_WORDS = set(en_file.read().splitlines())

result_dictionary = []

for word in EN_WORDS:
    if len(word) == 5:
        result_dictionary.append(word)

with open('app/static/words_5length.txt', 'w', encoding='utf-8') as out_file:
    for word in result_dictionary:
        out_file.write(word + '\n')
