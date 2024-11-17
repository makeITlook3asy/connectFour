class playingField():
    def __init__(self,height:int = 6,width:int = 7):
        self.height = height
        self.width = width
        self.area = list()

    def createEmptyField(self):
        for i in range(self.height):
            row = list()
            for j in range(self.width):
                row.append("_")
            self.area.append(row)

    def showField(self):
        print(" ")
        for row in range(self.height):
            print("|",end=" ")
            for col in range(self.width):
                print(self.area[row][col],end=" ")
            print("|")
        print(" ",end=" ")
        for col in range(1,self.width+1):
            print(col,end=" ")
        print(" ")


    def setStone(self,colNbr:int,color:str):
        for row in range(self.height - 1,-1,-1):
            if self.area[row][colNbr-1] == "_":
                self.area[row][colNbr-1] = color
                break
    
    def checkHorizonzal(self)->bool:
        for row in range(self.height):
            counter = 0
            for col in range(self.width-1):
                currentStone = self.area[row][col]
                nextStone = self.area[row][col+1]
                if currentStone == nextStone and currentStone != "_":
                    counter += 1
                else:
                    counter = 0
                if counter == 3:
                    print(f"{currentStone} wins")
                    return True
        return False


    def checkVertical(self):
        for col in range(self.width):
            counter = 0
            for row in range(self.height-1):
                currentStone = self.area[row][col]
                nextStone = self.area[row+1][col]
                if currentStone == nextStone and currentStone != "_":
                    counter += 1
                else:
                    counter = 0
                if counter == 3:
                    print(f"{currentStone} wins")
                    return True
        return False

    def checkDiago(self) -> bool:
        for row in range(self.height-3):
            for col in range(self.width-3):
                stones = list()
                for i in range(4):
                    stones.append(self.area[row+i][col+i])
                if "".join(stones) == "YYYY" or "".join(stones) == "RRRR":
                    print(f"{stones[0]} wins")
                    return True
        for row in range(self.height-3):
            for col in range(self.width-1,2,-1):
                stones = list()
                for i in range(4):
                    stones.append(self.area[row+i][col-i])
                if "".join(stones) == "YYYY" or "".join(stones) == "RRRR":
                    print(f"{stones[0]} wins")
                    return True
        return False
    
field = playingField()
field.createEmptyField()
field.showField()


isOver = False
run = 0
while not isOver:
    run += 1
    player = ["Red","R"] if run%2 != 0 else ["Yellow","Y"]
    newStoneCol = int(input(f"It is {player[0]}'s turn. Please type a value between 1 and {field.width}: "))
    if newStoneCol == 0:
        break
    field.setStone(newStoneCol,player[1])
    field.showField()
    isOver = field.checkHorizonzal() or field.checkVertical() or field.checkDiago()



