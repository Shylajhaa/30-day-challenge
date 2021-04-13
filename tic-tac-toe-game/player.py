class Player:
    def __init__(self, type):
        self._type = type
        self._cells = list()

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        self._type = type
    
    @property
    def cells(self):
        return self._cells
    
    def addCell(self, cell):
        self._cells.append(cell)