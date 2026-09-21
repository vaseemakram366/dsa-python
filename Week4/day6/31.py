class Solution:
    def resultArray(self, nums, k):
        result = [0] * k
        dp = [0] * k

        for num in nums:
            x = num % k
            new_dp = [0] * k

            new_dp[x] += 1

            for r in range(k):
                if dp[r]:
                    new_dp[(r * x) % k] += dp[r]

            dp = new_dp

            for r in range(k):
                result[r] += dp[r]

        return result  