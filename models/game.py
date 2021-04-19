import randomgaa

def play(gesture1, gesture2):
    gesture1 = gesture1.lower()
    gesture2 = gesture2.lower()
    if gesture1 == gesture2:
        return None
    if gesture1 == "rock" and gesture2 == "scissors":
        return "Player 1 wins by playing Rock"
    if gesture1 == 'scissors' and gesture2 == 'rock':
        return "Player 2 wins by playing Rock"
    if gesture1 == "rock" and gesture2 == "paper":
        return "Player 2 wins by playing Paper"
    if gesture1 == "paper" and gesture2 == "rock":
        return "Player 1 wins by playing Paper"
    if gesture1 == "paper" and gesture2 == "scissors":
        return "Player 2 wins by playing Scissors"
    if gesture1 == "scissors" and gesture2 == "paper":
        return "Player 1 wins by playing Scissors"
    return "Invalid input"

def generate_computer_gesture():
    gestures = ["rock", "paper", "scissors"]
    computer_gesture = random.choice(gestures)
    return computer_gesture

