# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : integer
    # @return a list of TreeNode
    def generateTrees(self, A):
        return self.generateTreesHelper(1, A)

    def generateTreesHelper(self, start, end):
        if start > end:
            return [None]
        res = []
        for i in range(start, end+1):
            left = self.generateTreesHelper(start, i-1)
            right = self.generateTreesHelper(i+1, end)
            for j in left:
                for k in right:
                    node = TreeNode(i)
                    node.left = j
                    node.right = k
                    res.append(node)
        return res
