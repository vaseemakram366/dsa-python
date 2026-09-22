class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        size = 1

        while size < n:
            size <<= 1

        prod = [1] * (2 * size)
        cnt = [[0] * k for _ in range(2 * size)]

        for i, v in enumerate(nums):
            v %= k
            p = size + i
            prod[p] = v
            cnt[p][v] = 1

        def merge(a, b):
            ap, ac = a
            bp, bc = b

            res = ac[:]

            for r in range(k):
                res[(ap * r) % k] += bc[r]

            return (ap * bp % k, res)

        for i in range(size - 1, 0, -1):
            prod[i], cnt[i] = merge(
                (prod[i * 2], cnt[i * 2]),
                (prod[i * 2 + 1], cnt[i * 2 + 1])
            )

        def update(pos, value):
            p = size + pos
            value %= k

            prod[p] = value
            cnt[p] = [0] * k
            cnt[p][value] = 1

            p >>= 1

            while p:
                prod[p], cnt[p] = merge(
                    (prod[p * 2], cnt[p * 2]),
                    (prod[p * 2 + 1], cnt[p * 2 + 1])
                )
                p >>= 1

        def query(l, r):
            left = (1, [0] * k)
            right = (1, [0] * k)

            l += size
            r += size

            while l <= r:
                if l & 1:
                    left = merge(left, (prod[l], cnt[l]))
                    l += 1

                if not (r & 1):
                    right = merge((prod[r], cnt[r]), right)
                    r -= 1

                l >>= 1
                r >>= 1

            return merge(left, right)[1]

        ans = []

        for index, value, start, x in queries:
            update(index, value)
            counts = query(start, n - 1)
            ans.append(counts[x])

        return ans