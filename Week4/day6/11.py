# 3568. Minimum Moves to Clean the Classroom

from collections import deque


class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        maxEnergy = energy

        litterBit = [[-1] * n for _ in range(m)]
        litterCount = 0
        startR = 0
        startC = 0

        # Find starting position and assign bits to litter
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    startR = r
                    startC = c

                elif classroom[r][c] == 'L':
                    litterBit[r][c] = litterCount
                    litterCount += 1

        allCollected = (1 << litterCount) - 1

        if litterCount == 0:
            return 0

        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]

        # visited[row][col][energyLeft][collectedMask]
        visited = [
            [
                [
                    [False] * (1 << litterCount)
                    for _ in range(maxEnergy + 1)
                ]
                for _ in range(n)
            ]
            for _ in range(m)
        ]

        que = deque()

        # (row, col, energyLeft, collectedMask)
        que.append((startR, startC, maxEnergy, 0))

        visited[startR][startC][maxEnergy][0] = True

        moves = 0

        while que:
            currSize = len(que)

            for _ in range(currSize):

                row, col, energyLeft, collectedMask = que.popleft()

                if collectedMask == allCollected:
                    return moves

                if energyLeft == 0:
                    continue

                for dr, dc in directions:

                    nextRow = row + dr
                    nextCol = col + dc

                    # Boundary check
                    if (
                        nextRow < 0 or nextRow >= m or
                        nextCol < 0 or nextCol >= n
                    ):
                        continue

                    cell = classroom[nextRow][nextCol]

                    # Obstacle
                    if cell == 'X':
                        continue

                    nextEnergy = energyLeft - 1
                    nextCollectedMask = collectedMask

                    # Recharge energy
                    if cell == 'R':
                        nextEnergy = maxEnergy

                    # Collect litter
                    elif cell == 'L':
                        nextCollectedMask |= (
                            1 << litterBit[nextRow][nextCol]
                        )

                    # Check if state already visited
                    if not visited[nextRow][nextCol][nextEnergy][nextCollectedMask]:

                        visited[nextRow][nextCol][nextEnergy][nextCollectedMask] = True

                        que.append(
                            (
                                nextRow,
                                nextCol,
                                nextEnergy,
                                nextCollectedMask
                            )
                        )

            moves += 1

        return -1