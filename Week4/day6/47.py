from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str):
        def is_valid(x):
            balance = 0

            for ch in x:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = deque([s])
        visited = {s}
        result = []

        while queue:
            found = False

            for _ in range(len(queue)):
                curr = queue.popleft()

                if is_valid(curr):
                    result.append(curr)
                    found = True

                if found:
                    continue

                for i in range(len(curr)):
                    if curr[i] not in "()":
                        continue

                    nxt = curr[:i] + curr[i + 1:]

                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)

            if found:
                return result

        return [""]