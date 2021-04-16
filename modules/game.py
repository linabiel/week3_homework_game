class Game:
    
    def compare_choices(self, player1, player2):
        if player1.choise == player2.choise:
            return None
        else:
            if player1.choice == "Rock" and player2.choice == "Scissors":
                return player1
            if player1.choice == "Rock" and player2.choice == "Paper":
                return player2
            if player1.choice == "Paper" and player2.choice == "Scissors":
                return player2

