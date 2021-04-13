import sys
sys.path.append(".")

from cell import Cell
from grid import Grid
from player import Player

print("Welcome")

playerX = Player('X')
playerO = Player('O')

grid = Grid(3)
grid.addPlayer(playerX)
grid.addPlayer(playerO)

isGameOver = False
players = grid.players

while not isGameOver:
    start = 0
    
    while start < 2 and not isGameOver:
        player = players[start]
        print("Hello " + player.type + ": Enter the cell")
        coordinates = input().split(',')

        cell = Cell(coordinates[0], coordinates[1], player.type)

        if grid.updateCell(cell) == False:
            continue

        result = grid.play()
        
        grid.display()

        if result is not None:
            isGameOver = True
            grid.printResult(player, result)

        start += 1
