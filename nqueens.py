import colorama
from colorama import Back

class nQueenSolver:
    solCount = 1

    def isSafeToPlace(self, row, col, board):
        for i in range(col):
            if board[row][i] == "♛":
                return False
        
        i = row-1
        j = col-1
        while(i>=0 and j>=0):
            if board[i][j] == "♛":
                return False
            i -= 1
            j -= 1
            
        i = row
        j = col      
        while(i < len(board) and j>=0):
            if board[i][j] == "♛":
                return False
            i += 1
            j -= 1
    
        return True
    
    def rf(self, col, board, size, allBoards):
        if col == size:
            print(Back.RESET+"Solution No. ", self.solCount,": ")
            one = Back.WHITE
            two = Back.RESET
            for row in board:
                for c in row:
                    print(one+" "+c+" "+two, end = "")
                    one, two = two, one
                print(Back.RESET)
                
                if size & 1 == 0:
                    one, two = two, one
            print()
            self.solCount+=1
            return
        
        for row in range(size):
            if self.isSafeToPlace(row, col, board):
                temp = board[row]
                board[row] = " " * col + "♛" + " "*(size-1-col)
                self.rf(col+1, board, size, allBoards)
                board[row] = temp
        
    def solveNQueens(self, n):
        board = [" "*n for i in range(n)]
        allBoards = []
        self.rf(0, board, n, allBoards)
        return allBoards

nqs = nQueenSolver()
n = int(input("\nEnter the value of n: "))
solutions = nqs.solveNQueens(n)