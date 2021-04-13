class Cell:
    def __init__(self, xCor, yCor, value):
        self._xCor = int(xCor)
        self._yCor = int(yCor)
        self._value = value
    
    @property
    def xCor(self):
        return self._xCor
        
    @xCor.setter
    def xCor(self, xCor):
        self._xCor = xCor
    
    @property
    def yCor(self):
        return self._yCor
        
    @yCor.setter
    def yCor(self, yCor):
        self._yCor = yCor
    
    @property
    def value(self):
        return self._value
        
    @value.setter
    def value(self, value):
        self._value = value