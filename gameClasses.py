"""
Spielfeld:
    -> 6 x 7
    -> Funktion um Stein zu legen
"""

class playingField():
    def __init__(self,height:int = 6,width:int = 7):
        self.height = height
        self.width = width
        self.area = list()

    def createEmptyField(self):
        for i in range(self.height):
            row = list()
            for j in range(self.width):
                row.append("X")
            self.area.append(row)

    def showField(self):
        print(" ")
        for row in range(self.height):
            print("|",end=" ")
            for col in range(self.width):
                print(self.area[row][col],end=" ")
            print("|")
        print(" ")

    def setStone(self,colNbr:int,color:str):
        for row in range(self.height - 1,-1,-1):
            if self.area[row][colNbr-1] == "X":
                self.area[row][colNbr-1] = color
                break

field = playingField()
field.createEmptyField()
field.showField()
field.setStone(3,'R')
field.showField()
field.setStone(3,'R')
field.showField()


