# 2091. Removing Minimum and Maximum From Array

class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Make min_idx the smaller index
        if min_idx > max_idx:
            min_idx, max_idx = max_idx, min_idx

        # Case 1: Remove both from the left
        left = max_idx + 1

        # Case 2: Remove both from the right
        right = n - min_idx

        # Case 3: Remove min from left and max from right
        both = (min_idx + 1) + (n - max_idx)

        return min(left, right, both)