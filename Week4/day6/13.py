# 3876. Construct Uniform Parity Array II

class Solution:
    def uniformArray(self, nums1):
        min_odd = float('inf')

        # Find the smallest odd number
        for x in nums1:
            if x % 2 == 1:
                min_odd = min(min_odd, x)

        # No odd numbers -> all are even
        if min_odd == float('inf'):
            return True

        # Check if any even number is smaller
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False

        return True