class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # A palindrome can have at most one odd count
        odd = 0
        middle = ""

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                middle = chr(i + ord('a'))

        if odd > 1:
            return ""

        # Characters available for the left half
        half = [c // 2 for c in cnt]

        half_len = n // 2

        # Build the left half
        left = []

        def make_palindrome():
            left_str = ''.join(left)

            if n % 2 == 1:
                return left_str + middle + left_str[::-1]
            else:
                return left_str + left_str[::-1]

        def dfs(pos, greater):
            if pos == half_len:
                result = make_palindrome()

                if result > target:
                    return result

                return None

            # If already greater, choose smallest available character
            if greater:
                start = 0
            else:
                start = ord(target[pos]) - ord('a')

            for c in range(start, 26):

                if half[c] == 0:
                    continue

                # If we are still equal to target,
                # don't choose a character smaller than target[pos].
                if not greater and c < start:
                    continue

                half[c] -= 1
                left.append(chr(c + ord('a')))

                new_greater = greater or (c > start)

                result = dfs(pos + 1, new_greater)

                if result is not None:
                    return result

                left.pop()
                half[c] += 1

            return None

        result = dfs(0, False)

        return result if result is not None else ""