# 3870. Count Commas in Range

class Solution:
    def countCommas(self, n: int) -> int:
        # Numbers from 1,000 to 99,999 have exactly 1 comma
        if n < 1000:
            return 0

        # Numbers from 1,000 to n
        return n - 999