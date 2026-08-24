# Stone Game VIII
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        # Prefix sums in-place
        for i in range(1, n):
            stones[i] += stones[i - 1]

        # dp[n - 1]
        best = stones[n - 1]

        # We stop at i = 1 because the first move
        # must take at least 2 stones.
        for i in range(n - 2, 0, -1):
            best = max(best, stones[i] - best)

        return best