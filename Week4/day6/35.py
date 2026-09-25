class Solution:
    def __init__(self):
        self.s = ""
        self.n = 0
        self.idx = 0

    def getUnit(self):
        result = {" "}

        if self.s[self.idx] == '{':
            self.idx += 1
            result = self.performUnion()
        else:
            result = {self.s[self.idx]}

        self.idx += 1

        return result

    def performConcat(self):
        result = {""}

        while self.idx < self.n and (
            self.s[self.idx] == '{' or self.s[self.idx].isalpha()
        ):
            temp = self.getUnit()

            concatResult = set()

            for left in result:
                for right in temp:
                    concatResult.add(left + right)

            result = concatResult

        return result

    def performUnion(self):
        result = set()

        while True:
            temp = self.performConcat()
            result.update(temp)

            if self.idx < self.n and self.s[self.idx] == ',':
                self.idx += 1
            else:
                break

        return result

    def braceExpansionII(self, expression):
        self.s = expression
        self.n = len(expression)
        self.idx = 0

        st = self.performUnion()

        return sorted(st)