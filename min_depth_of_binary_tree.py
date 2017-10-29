# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):
        if A is None:
            return 0
        if A.left is None and A.right is None:
            return 1
        child_depths = [self.minDepth(A.left), self.minDepth(A.right)]
        if 0 in child_depths:
            return 1 + max(child_depths)
        else:
            return 1 + min(child_depths)
