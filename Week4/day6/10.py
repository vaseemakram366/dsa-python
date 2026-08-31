# 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

class Solution:
    def nodesBetweenCriticalPoints(self, head):
        # Less than 3 nodes cannot have a critical point
        if head is None or head.next is None or head.next.next is None:
            return [-1, -1]

        prev = head
        curr = head.next

        pos = 1
        first = -1
        last = -1
        minDistance = float('inf')

        while curr.next is not None:

            # Check for local maximum or local minimum
            isMax = curr.val > prev.val and curr.val > curr.next.val
            isMin = curr.val < prev.val and curr.val < curr.next.val

            if isMax or isMin:

                # First critical point
                if first == -1:
                    first = pos

                else:
                    # Distance from previous critical point
                    minDistance = min(minDistance, pos - last)

                # Update last critical point
                last = pos

            prev = curr
            curr = curr.next
            pos += 1

        # Fewer than 2 critical points
        if first == -1 or first == last:
            return [-1, -1]

        # Maximum distance
        maxDistance = last - first

        return [minDistance, maxDistance]