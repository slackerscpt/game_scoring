import random
from winsound import PlaySound


class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.score = 0

    def updateScore(self, score):
        self.score += score
    def printScore(self):
        print(self.name,"Score is:",self.score)

class Game:
    def __init__(self):
        self.maxScore = 500

    def setMaxScore(self, number):
        self.maxScore = number

    def checkScore(self, playerScore):
        if self.maxScore >= playerScore:
            return True
        return False

currentGame = Game()
currentGame.setMaxScore(50)
player1 = Player("Josh", 1)

player1.updateScore(40)
player1.printScore()
if not currentGame.checkScore(player1.score):
    print ('Game Over')

print ('Round 2')
player1.updateScore(20)
player1.printScore()

if not currentGame.checkScore(player1.score):
    print ('Game Over')


    
