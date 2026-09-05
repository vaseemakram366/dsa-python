# 3904. Smallest Stable Index II

class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # min_from[i] = minimum element from i to n-1
        min_from = [0] * n

        min_el = float('inf')

        for i in range(n - 1, -1, -1):
            min_el = min(min_el, nums[i])
            min_from[i] = min_el

        # Maximum element from 0 to i
        max_el = float('-inf')

        for i in range(n):
            max_el = max(max_el, nums[i])

            instability = max_el - min_from[i]

            if instability <= k:
                return i

        return -1