
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mp = {}

        for key, value in knowledge:
            mp[key] = value

        result = []
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                j = s.find(')', i + 1)
                temp = s[i + 1:j]
                result.append(mp.get(temp, '?'))
                i = j
            else:
                result.append(s[i])

            i += 1

        return ''.join(result)

