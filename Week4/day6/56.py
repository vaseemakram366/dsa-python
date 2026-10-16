
class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree_sum = [0] * (4 * n + 5)
        tree_sq = [0] * (4 * n + 5)
        lazy = [0] * (4 * n + 5)

        def apply(node, l, r, val):
            length = r - l + 1

            tree_sq[node] = (
                tree_sq[node]
                + 2 * val * tree_sum[node]
                + val * val * length
            ) % MOD

            tree_sum[node] = (
                tree_sum[node] + val * length
            ) % MOD

            lazy[node] = (lazy[node] + val) % MOD

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return

            mid = (l + r) // 2
            val = lazy[node]

            apply(node * 2, l, mid, val)
            apply(node * 2 + 1, mid + 1, r, val)

            lazy[node] = 0

        def update(node, l, r, ql, qr):
            if ql > r or qr < l:
                return

            if ql <= l and r <= qr:
                apply(node, l, r, 1)
                return

            push(node, l, r)

            mid = (l + r) // 2

            update(node * 2, l, mid, ql, qr)
            update(node * 2 + 1, mid + 1, r, ql, qr)

            tree_sum[node] = (
                tree_sum[node * 2]
                + tree_sum[node * 2 + 1]
            ) % MOD

            tree_sq[node] = (
                tree_sq[node * 2]
                + tree_sq[node * 2 + 1]
            ) % MOD

        last = {}
        ans = 0

        for r, x in enumerate(nums):
            prev = last.get(x, -1)

            update(1, 0, n - 1, prev + 1, r)

            last[x] = r
            ans = (ans + tree_sq[1]) % MOD

        return ans
