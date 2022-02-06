""" Wordle Helper logic. """
import random
import timeit

# Load the Word list with only 5 length words from text file.
EN_FILENAME = './app/static/words_5length.txt'
with open(EN_FILENAME, encoding='utf-8') as en_file:
    EN_WORDS = set(en_file.read().splitlines())


class Hand:
    """ Class to represent the letters that we have. """
    def __init__(self, letterset, lettercount):
        self.letterset = letterset
        self.lettercount = lettercount
        self.held_letters = self.draw_letters(lettercount)

    def draw_letters(self, lettercount: int) -> list:
        """ Draw a number of random letters from the letter set. """
        if lettercount >= 2:
            print(self.letterset)
            ownletters = random.sample(self.letterset, k=lettercount)
            print(f'letters drawn: {ownletters}')
            return ownletters
        print('ERROR: letter number less than 2!')
        return []

    def update_hand(self, letters):
        """ Update Hand with custom letters. """
        self.held_letters = letters


class Wordle:
    """ Class to represent Wordle helper logic. """
    def __init__(self):
        self.wordlist = EN_WORDS
        self.letterset = ['a'] * 2 + ['b'] * 2 + ['c'] * 2 + ['d'] * 2 + ['e'] * 2 + ['f'] * 2 + \
                         ['g'] * 2 + ['h'] * 2 + ['i'] * 2 + ['j'] * 2 + ['k'] * 2 + ['l'] * 2 + \
                         ['m'] * 2 + ['n'] * 2 + ['o'] * 2 + ['p'] * 2 + ['q'] * 2 + ['r'] * 2 + \
                         ['s'] * 2 + ['t'] * 2 + ['u'] * 2 + ['v'] * 2 + ['w'] * 2 + ['x'] * 2 + \
                         ['y'] * 2 + ['z'] * 2
        self.hand = Hand(self.letterset, 7)

    def checker(self, ownletters, length):
        """ Check which "length" length words of the dictionary can be built from held letters. """
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
