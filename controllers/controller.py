from flask import render_template, request
from app import app
from modules.game import play

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/<gesture1>/<gesture2>')
def enter_gestures_into_url(gesture1, gesture2):
    return render_template('url.html', winner=play(gesture1, gesture2))

@app.route('/play', methods=['POST', 'GET'])
def play_game():
    return render_template('play.html', title='Home')
