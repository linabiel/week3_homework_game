from flask import render_template, request
from app import app
from models.game import play, generate_computer_gesture

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<gesture1>/<gesture2>')
def enter_gestures_into_url(gesture1, gesture2):
    return render_template('url.html', winner=play(gesture1, gesture2))

@app.route('/play')
def select_gesture_get():
    return render_template('play_use_select.html')

@app.route('/play', methods=['POST'])
def select_gesture():
    gesture1 = request.form['gesture1']
    gesture2 = request.form['gesture2']
    return render_template('url.html', winner=play(gesture1, gesture2))

@app.route('/comp')
def play_against_computer_get():
    return render_template('play_with_computer.html')

@app.route('/comp', methods=['POST'])
def play_against_computer():
    gesture1 = generate_computer_gesture()
    gesture2 = request.form['gesture2']
    return render_template('com_vs_you_win_page.html',
                           winner=play(gesture1, gesture2), computer_gesture=gesture1.capitalize())
