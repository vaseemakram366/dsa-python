class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = n + 1
        best = INF
        ans = INF

        left = 0
        curr = 0
        min_len = [INF] * n

        for right in range(n):
            curr += arr[right]

            while curr > target:
                curr -= arr[left]
                left += 1

            if curr == target:
                length = right - left + 1

                if left > 0 and min_len[left - 1] != INF:
                    ans = min(ans, length + min_len[left - 1])

                best = min(best, length)

            min_len[right] = best

        return -1 if ans == INF else ans