# 2904. Shortest and Lexicographically Smallest Beautiful String


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        ans = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            # We have more than k ones
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            # Exactly k ones
            if ones == k:
                # Remove unnecessary leading zeros
                while s[left] == '0':
                    left += 1

                curr = s[left:right + 1]

                if (ans == "" or
                    len(curr) < len(ans) or
                    (len(curr) == len(ans) and curr < ans)):
                    ans = curr

        return ans