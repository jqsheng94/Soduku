class soduku():
    def __init__(self, **kwargs):
        self.grid = kwargs.get("grid")
        self.backtracks = 0

    # This procedure finds the next empty square to fill on the Sudoku grid
    def findNextCellToFill(self):
        # Look for an unfilled grid location
        for x in range(0, 9):
            for y in range(0, 9):
                if self.grid[x][y] == 0:
                    return x, y
        return -1, -1

    # This procedure checks if setting the (i, j) square to e is valid
    def isValid(self, i, j, e):
        rowOk = all([e != self.grid[i][x] for x in range(9)])
        if rowOk:
            columnOk = all([e != self.grid[x][j] for x in range(9)])
            if columnOk:
                # finding the top left x,y co-ordinates of
                # the section or sub-grid containing the i,j cell
                secTopX, secTopY = 3 * (i // 3), 3 * (j // 3)
                for x in range(secTopX, secTopX + 3):
                    for y in range(secTopY, secTopY + 3):
                        if self.grid[x][y] == e:
                            return False
                return True
        return False

    # This procedure fills in the missing squares of a Sudoku puzzle
    # obeying the Sudoku rules through brute-force guessing and checking
    def solveSudoku(self):
        # find the next cell to fill
        i, j = self.findNextCellToFill()
        if i == -1:
            return True
        for e in range(1, 10):
            # Try different values in i, j location
            if self.isValid(i, j, e):
                self.grid[i][j] = e
                if self.solveSudoku():
                    return True
                # Undo the current cell for backtracking
                self.backtracks += 1
        self.grid[i][j] = 0
        return False

    def printSudoku(self):
        self.solveSudoku()
        numrow = 0
        for row in self.grid:
            if numrow % 3 == 0 and numrow != 0:
                print(' ')
            print(row[0:3], ' ', row[3:6], ' ', row[6:9])
            numrow += 1
        return


















diff =  [[5, 1, 7, 6, 0, 0, 0, 3, 4],[2, 8, 9, 0, 0, 4, 0, 0, 0],[3, 4, 6, 2, 0, 5, 0, 9, 0],[6, 0, 2, 0, 0, 0, 0, 1, 0],[0, 3, 8, 0, 0, 6, 0, 4, 7],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 9, 0, 0, 0, 0, 0, 7, 8], [7, 0, 3, 4, 0, 0, 5, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
A = soduku(grid = diff).printSudoku()
print(A)
