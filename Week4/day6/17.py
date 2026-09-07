# 940. Distinct Subsequences II

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = [0] * 26
        total = 0

        for ch in s:
            i = ord(ch) - ord('a')

            # Every existing subsequence can append ch
            # + the subsequence consisting only of ch
            new = (total + 1) % MOD

            # Replace previous subsequences ending with ch
            total = (total + new - dp[i]) % MOD
            dp[i] = new

        return total