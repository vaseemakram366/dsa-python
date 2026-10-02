class Solution:
    def __init__(self):
        self.result = []

    def solve(self, curr, n, open, close):
        if len(curr) == 2 * n:
            self.result.append(curr)
            return

        if open < n:
            self.solve(curr + "(", n, open + 1, close)

        if close < open:
            self.solve(curr + ")", n, open, close + 1)

    def generateParenthesis(self, n):
        self.result = []
        self.solve("", n, 0, 0)
        return self.result