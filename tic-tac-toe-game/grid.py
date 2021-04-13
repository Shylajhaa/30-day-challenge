import sys
sys.path.append(".")

from cell import Cell

class Grid:
    DRAW = "draw"
    WIN = "win"
    
    def __init__(self, size):
        self._size = size
        self._players = list()
        self._cells = [[Cell(i, j, '0') for j in range(size)] for i in range(size)]

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size
  
    @property
    def players(self):
        return self._players

    def addPlayer(self, player):
        self._players.append(player)
    
    @property
    def cells(self):
        return self._cells
  
    def updateCell(self, cell):
        if self._cells[cell.xCor][cell.yCor].value != '0':
            print("Cell already taken")
            return False
        
        self._cells[cell.xCor][cell.yCor] = cell
    
    def isFull(self):
        hasEmptyCell = False
        
        for i in range(self._size):
            for j in range(self._size):
                if self._cells[i][j].value == '0':
                    hasEmptyCell = True
                    break
        
            if hasEmptyCell:
                break
        
        return not hasEmptyCell
    
    def isLineDrawn(self, player, i, j):
        if i == self._size or j == self._size:
            print(i, j)
            return True

        if self._cells[i][j].value != player.type:
            return False
        
        return self.isLineDrawn(player, i+1, j) or self.isLineDrawn(player, i, j+1) or self.isLineDrawn(player, i+1, j+1)


    def checkWin(self, player):
        for i in range(self._size):
            for j in range(self.size):
                if i > 0 and j > 0:
                    continue

                if self.isLineDrawn(player, i, j):
                    return True
        
        return False
    
    def play(self):
        for player in self._players:
            if self.checkWin(player):
                return self.WIN
    
        if self.isFull():
            return self.DRAW
    
    def display(self):
        for i in range(self._size):
            for j in range(self._size):
                print(self._cells[i][j].value + " ", end='')
            print("")
    
    def printResult(self, player, result):
        if result == self.DRAW:
            print("The game is a draw!!")
        elif result == self.WIN:
            print(player.type + " Wins!!")