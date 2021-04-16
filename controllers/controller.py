from flask import render_template, request
from app import app
from modules import player
from modules.game import compare_choices

@app.route('/game')
def index():
    return render_template('index.html', title='Home')


@app.route('/game', methods=['POST'])
def play_game(self):
    player1 = request.form['gesture1']
    player2 = request.form['gesture2']
    compare_choices(self, player1, player2)