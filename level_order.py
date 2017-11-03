# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        from collections import deque
        self.queue = deque([A])
        result = []
        while len(self.queue):
            result.append(self.traverseLevel())
        return result

    def traverseLevel(self):
        new_queue = []
        result = []
        while len(self.queue):
            node = self.queue.popleft()
            result.append(node.val)
            if node.left is not None:
                new_queue.append(node.left)
            if node.right is not None:
                new_queue.append(node.right)
        self.queue.extend(new_queue)
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(2)
    print Solution().levelOrder(root)
