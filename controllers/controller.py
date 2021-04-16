from flask import render_template, request
from app import app
from modules.game import play

@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/<gesture1>/<gesture2>')
def play_game(gesture1, gesture2):
    return render_template('play.html', winner=play(gesture1, gesture2))
