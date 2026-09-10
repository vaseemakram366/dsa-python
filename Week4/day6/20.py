# 2265. Count Nodes Equal to Average of Subtree

class Solution:
    def __init__(self):
        self.result = 0

    def solve(self, root):
        if not root:
            return (0, 0)

        leftSum, leftCount = self.solve(root.left)
        rightSum, rightCount = self.solve(root.right)

        totalSum = leftSum + rightSum + root.val
        totalCount = leftCount + rightCount + 1

        avg = totalSum // totalCount

        if avg == root.val:
            self.result += 1

        return (totalSum, totalCount)

    def averageOfSubtree(self, root):
        self.result = 0
        self.solve(root)
        return self.result