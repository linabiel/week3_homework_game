from flask import render_template, request
from app import app
from modules.game import play

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<gesture1>/<gesture2>')
def enter_gestures_into_url(gesture1, gesture2):
    return render_template('url.html', winner=play(gesture1, gesture2))

@app.route('/play')
def select_gesture_get():
    return render_template('play.html')

@app.route('/play', methods=['POST'])
def select_gesture():
    gesture1 = request.form["gesture1"]
    gesture2 = request.form['gesture2']
    print(gesture1)
    print(gesture2)
    print(play(gesture1, gesture2))
    return render_template('url.html', winner=play(gesture1, gesture2))
