# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        result = []
        if A is None:
            return result

        next_level = [A]
        direction = 'lr'

        while len(next_level):
            next_next_level = []
            current_level = []
            for node in next_level:
                if node.left:
                    next_next_level.append(node.left)
                if node.right:
                    next_next_level.append(node.right)
                current_level.append(node.val)
            if direction == 'rl':
                current_level = current_level[::-1]
            if len(current_level):
                result.append(current_level)
            direction = direction[::-1]
            next_level = next_next_level
        return result


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print Solution().zigzagLevelOrder(tree)