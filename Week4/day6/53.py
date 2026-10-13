from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted(x * x for x in nums)
        n = len(sq)
        minus = n // 2  # number of smallest values to subtract
        return sum(sq[minus:]) - sum(sq[:minus])