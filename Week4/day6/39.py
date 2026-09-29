class Solution:
    def hasValidPath(self, grid):
        self.m = len(grid)
        self.n = len(grid[0])

        if (self.m + self.n - 1) % 2 == 1:
            return False

        if grid[0][0] == ')' or grid[self.m - 1][self.n - 1] == '(':
            return False

        self.t = [[[-1] * 201 for _ in range(self.n)] for _ in range(self.m)]

        return self.solve(0, 0, 0, grid)

    def solve(self, i, j, openCount, grid):
        if grid[i][j] == '(':
            openCount += 1
        else:
            openCount -= 1

        if openCount < 0:
            return False

        if self.t[i][j][openCount] != -1:
            return self.t[i][j][openCount]

        if i == self.m - 1 and j == self.n - 1:
            self.t[i][j][openCount] = (openCount == 0)
            return self.t[i][j][openCount]

        # Move down
        if i + 1 < self.m:
            if self.solve(i + 1, j, openCount, grid):
                self.t[i][j][openCount] = True
                return True

        # Move right
        if j + 1 < self.n:
            if self.solve(i, j + 1, openCount, grid):
                self.t[i][j][openCount] = True
                return True

        self.t[i][j][openCount] = False
        return False