from typing import List
from collections import deque



class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        seen = [False] * n
        complete = 0

        for start in range(n):
            if seen[start]:
                continue

            q = deque([start])
            seen[start] = True

            nodes = []
            edge_count = 0

            while q:
                cur = q.popleft()
                nodes.append(cur)
                edge_count += len(adj[cur])

                for nxt in adj[cur]:
                    if not seen[nxt]:
                        seen[nxt] = True
                        q.append(nxt)

            size = len(nodes)
            edge_count //= 2

            if edge_count == size * (size - 1) // 2:
                complete += 1

        return complete