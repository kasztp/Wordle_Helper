from copy import deepcopy
import re
from flask import render_template, flash, redirect, request, url_for
from app import app
from .forms import ConfigForm
from .wordle_logic import Wordle

max_word_length = 5
letter_draw = []
grouped = {}


@app.route('/')
def root():
    return render_template('results.html', title='Home', scores=grouped,
                           letters='letters')


@app.route('/results')
def index():
    return render_template('results.html', title='Home', scores=grouped,
                           letters=letter_draw)


@app.route('/config', methods=['GET', 'POST'])
def config():
    form = ConfigForm()
    if form.validate_on_submit():
        if request.method == 'POST':
            game = Wordle()
            global letter_draw
            letter_draw = []
            if form.own_letterset.data:
                form.own_letterset.data = re.sub(r'\W+', '', form.own_letterset.data).lower()
                for character in form.own_letterset.data:
                    letter_draw += [character]
                game.hand.update_hand(letter_draw)
            else:
                letter_draw = game.hand.held_letters
            print(f'Letters drawn: {letter_draw}')
            flash(f'Letters: {letter_draw}')
            valid_words = game.word_check(letter_draw, max_word_length)

            if form.placed_letters.data:
                print(form.placed_letters.data)
                temp_word_list = deepcopy(valid_words)
                for idx, word in enumerate(temp_word_list):
                    temp_word = list(word)
                    for place, letter in enumerate(form.placed_letters.data):
                        if letter != '' and letter != temp_word[place]:
                            valid_words.discard(word)

            if form.guessed_letters.data:
                print(form.guessed_letters.data)
                temp_word_list = deepcopy(valid_words)
                guessed_letters = list(form.guessed_letters.data)
                for idx, word in enumerate(temp_word_list):
                    for letter in guessed_letters:
                        if letter not in word:
                            valid_words.discard(word)

            global grouped
            grouped = {}
            if valid_words != 'NONE':
                scores = game.score_calc(valid_words)
                grouped = game.group_by_score(scores)
            else:
                grouped = {0: 'Number of valid words found'}
        return redirect(url_for('index'))
    return render_template('config.html', title='Configuration', form=form)
