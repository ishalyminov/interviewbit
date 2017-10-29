# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        if A is None:
            return 0
        if A.left is None and A.right is None:
            return 1
        child_depths = [self.maxDepth(A.left), self.maxDepth(A.right)]
        return 1 + max(child_depths)
