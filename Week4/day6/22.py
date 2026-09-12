from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        arr = sorted(
            [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        )

        starts = [x[0] for x in arr]

        nxt = [0] * n
        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])

        dp = [[None] * 5 for _ in range(n + 1)]

        for k in range(5):
            dp[n][k] = (0, ())

        for i in range(n - 1, -1, -1):
            l, r, w, idx = arr[i]

            for k in range(1, 5):
                skip = dp[i + 1][k]

                take_score, take_indices = dp[nxt[i]][k - 1]
                take = (
                    take_score + w,
                    tuple(sorted((idx,) + take_indices))
                )

                if take[0] > skip[0]:
                    dp[i][k] = take
                elif take[0] < skip[0]:
                    dp[i][k] = skip
                else:
                    dp[i][k] = min(take, skip)

        return list(dp[0][4][1])