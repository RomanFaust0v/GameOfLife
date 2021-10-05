from Game import Game
from Board import Board

size = (50, 50)
board = Board(size)
screenSize = (800, 700)
game = Game(board, screenSize)
game.run()
