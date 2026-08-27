class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        cnt = Counter(s)
        n = len(s)

        def build_greater(pos):
            # Try to make the answer equal to target
            # until we can make it greater.
            for i in range(pos, n):
                # First try to put target[i]
                if cnt[target[i]] > 0:
                    cnt[target[i]] -= 1
                    continue

                # target[i] is unavailable.
                # We must choose the smallest character greater than target[i].
                for c in sorted(cnt):
                    if c > target[i] and cnt[c] > 0:
                        cnt[c] -= 1

                        # Fill the remaining positions minimally
                        ans = target[:i] + c
                        for ch in sorted(cnt):
                            ans += ch * cnt[ch]

                        return ans

                # Cannot make it greater here.
                return ""

            # s can form exactly target, but we need STRICTLY greater.
            return ""

        # Try matching target from the beginning.
        for i in range(n):
            if cnt[target[i]] > 0:
                cnt[target[i]] -= 1
            else:
                # target[i] cannot be matched.
                # Find the smallest possible character > target[i].
                for c in sorted(cnt):
                    if c > target[i] and cnt[c] > 0:
                        cnt[c] -= 1

                        ans = target[:i] + c

                        for ch in sorted(cnt):
                            ans += ch * cnt[ch]

                        return ans

                # No greater character here.
                break

        # We matched a prefix but couldn't make it greater.
        # Backtrack and increase an earlier character.
        cnt = Counter(s)

        for i in range(n - 1, -1, -1):
            # Use target[0:i] as prefix.
            cnt = Counter(s)

            possible = True

            for j in range(i):
                if cnt[target[j]] == 0:
                    possible = False
                    break
                cnt[target[j]] -= 1

            if not possible:
                continue

            # At position i, choose smallest char > target[i]
            for c in sorted(cnt):
                if c > target[i] and cnt[c] > 0:
                    cnt[c] -= 1

                    ans = target[:i] + c

                    for ch in sorted(cnt):
                        ans += ch * cnt[ch]

                    return ans

        return ""