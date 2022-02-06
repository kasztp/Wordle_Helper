import random
import timeit

# Load Word dictionaries from text files.
EN_FILENAME = './app/static/words.txt'  # Scrabble (for now) EN word list
with open(EN_FILENAME, encoding='utf-8') as en_file:
    EN_WORDS = set(en_file.read().splitlines())


class Hand:
    def __init__(self, letterset, lettercount):
        self.letterset = letterset
        self.lettercount = lettercount
        self.held_letters = self.draw_letters(lettercount)

    # Draw n number of random letters from the letter set
    def draw_letters(self, lettercount: int) -> list:
        if lettercount >= 2:
            print(self.letterset)
            ownletters = random.sample(self.letterset, k=lettercount)
            print(f'letters drawn: {ownletters}')
            return ownletters
        else:
            print('ERROR: letter number less than 2!')
            return []

    def update_hand(self, letters):
        self.held_letters = letters


class Wordle:
    def __init__(self):
        self.wordlist = EN_WORDS
        self.letterset = ['a'] * 9 + ['b'] * 2 + ['c'] * 2 + ['d'] * 4 + ['e'] * 12 +\
                    ['f'] * 2 + ['g'] * 3 + ['h'] * 2 + ['i'] * 9 + ['j'] + ['k'] +\
                    ['l'] * 4 + ['m'] * 2 + ['n'] * 6 + ['o'] * 8 + ['p'] * 2 +\
                    ['q'] + ['r'] * 6 + ['s'] * 4 + ['t'] * 6 + ['u'] * 4 +\
                    ['v'] * 2 + ['w'] * 2 + ['x'] + ['y'] * 2 + ['z']
        self.hand = Hand(self.letterset, 7)

    # Check which words of the dictionary can be built from held letters (HU version to be polished):
    def checker(self, ownletters, length):
        valid_words = set()
        for word in self.wordlist:
            if len(word) == length:
                word = word.lower()
                characters = list(word)
                ownletters_tmp = ownletters.copy()
                matches = 0
                for character in characters:
                    if character in ownletters_tmp:
                        matches += 1
                        ownletters_tmp.remove(character)
                if matches == length:
                    valid_words.add(word)
        return valid_words

    def word_check(self, ownletters, length):
        textperm = set()
        start_time = timeit.default_timer()
        results = set(self.checker(ownletters, length))
        print(timeit.default_timer() - start_time)
        print(f'Unique {length} length words generated: {len(results)}')
        textperm |= results
        print(f'Unique words generated so far: {len(textperm)}')
        return textperm

    # Calculate word point values
    def score_calc(self, words: list) -> dict:
        if words != 1:
            scores = {}
            for word in words:
                if word != ():
                    value = len(word)
                    scores[word] = value
            return scores
        else:
            print('ERROR: NO valid words given!')
            return 'NONE'

    def group_by_score(self, scores: dict) -> dict:
        score_groups = sorted(set(val for val in scores.values()), reverse=True)
        grouped_words = {}
        for number in score_groups:
            wordgroup = []
            for i in scores.items():
                if i[1] == number:
                    wordgroup.extend(i[0:1])
            grouped_words[number] = sorted(wordgroup)
        return grouped_words
