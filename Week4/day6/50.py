class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2
            needed = sum(max(0, d - mid) for d in diff)

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        level = left
        remaining = k - sum(max(0, d - level) for d in diff)

        diff = [min(d, level) for d in diff]

        for i in range(len(diff)):
            if remaining > 0 and diff[i] == level:
                diff[i] -= 1
                remaining -= 1

        return sum(d * d for d in diff)