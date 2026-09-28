class Solution:
    def maxDepth(self, s: str) -> int:
        openBrackets = 0
        result = 0

        for ch in s:
            if ch == '(':
                openBrackets += 1
            elif ch == ')':
                openBrackets -= 1

            result = max(result, openBrackets)

        return result