from flask import render_template, request
from app import app
from modules import player
from modules.game import Game

@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/')
def play(player1, player2):
    player1 = request.form['gesture1']
    player2 = request.form['gesture2']
    game = Game()
    winner = game.compare_choices(player1, player2)
    return render_template('index.html', winner=game.compare_choices(player1, player2))