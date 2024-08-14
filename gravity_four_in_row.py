FIRST_PLAYER = 1
SECOND_PLAYER = 2
ONGOING = 0
DRAW = -3
INVALID_COL = -1
NO_SPACE = -2

class Gmok():
    def __init__(self, width=11, height=8):
        self.width = width
        self.height = height
        self.gameMap = [[0]*height for i in range(width)]

    def printMap(self):
        for i in range(self.height-1,-1,-1):
            for j in range(self.width):
                print(self.gameMap[j][i], end=' ')
            print()
        print('='*(self.width*2-1))
        print(' '.join([str(i) for i in list(range(self.width))]))
    
    def push(self, turn_number, column_number):
        if column_number < 0 or column_number >= self.width:
            return -1
        if 0 in self.gameMap[column_number]:
            self.gameMap[column_number][self.gameMap[column_number].index(0)] = turn_number
        else: return -2

        return self.gameState()
    
    # push return -1 : invalid column number
    # push return -2 : already filled
    # push return -3 : draw
    # push return 0 : game is ongoing
    # push return n : game ended by turn number n

    def gameState(self):
        # Check for four-in-a-row horizontally, vertically, or diagonally
        for col in self.gameMap:
            for i in range(self.height - 3):
                if col[i] == col[i+1] == col[i+2] == col[i+3] != 0:
                    return col[i]
        
        for row in range(self.height):
            for i in range(self.width - 3):
                if self.gameMap[i][row] == self.gameMap[i+1][row] == self.gameMap[i+2][row] == self.gameMap[i+3][row] != 0:
                    return self.gameMap[i][row]
        
        for i in range(self.width - 3):
            for j in range(self.height - 3):
                if self.gameMap[i][j] == self.gameMap[i+1][j+1] == self.gameMap[i+2][j+2] == self.gameMap[i+3][j+3] != 0:
                    return self.gameMap[i][j]
                if self.gameMap[i][j+3] == self.gameMap[i+1][j+2] == self.gameMap[i+2][j+1] == self.gameMap[i+3][j] != 0:
                    return self.gameMap[i][j+3]
        
        # Check for draw
        for col in self.gameMap:
            if 0 in col:
                return 0
        return -3
