# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        return self.inOrderSubtreeTraversal(A)

    def inOrderSubtreeTraversal(self, root):
        result = []
        if root is None:
            return result
        roots = self.goToStartOfSubtree(root)
        while len(roots):
            current_root = roots.pop()
            result.append(current_root.val)
            result += self.inOrderSubtreeTraversal(current_root.right)
        return result

    def goToStartOfSubtree(self, root):
        from collections import deque
        stack = deque([])
        pointer = root
        while pointer is not None:
            stack.append(pointer)
            pointer = pointer.left
        return stack


if __name__ == '__main__':
    tree = TreeNode(10)
    tree.left = TreeNode(0)
    tree.right = TreeNode(15)
    print Solution().inOrderSubtreeTraversal(tree)