# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        from collections import deque
        self.roots_stack = deque([])
        self.pointer = root
        self.goToStartOfSubtree(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.pointer is not None

    # @return an integer, the next smallest number
    def next(self):
        val = self.pointer.val
        if self.pointer.right is not None:
            self.goToStartOfSubtree(self.pointer.right)
        elif len(self.roots_stack):
            self.pointer = self.roots_stack.pop()
        else:
            self.pointer = None
        return val

    def goToStartOfSubtree(self, root):
        self.pointer = root
        if self.pointer is None:
            return
        while self.pointer.left is not None:
            self.roots_stack.append(self.pointer)
            self.pointer = self.pointer.left

    # Your BSTIterator will be called like this:
    # i = BSTIterator(root)
    # while i.hasNext(): print i.next(),

if __name__ == '__main__':
    root = TreeNode(0)
    # root.left = TreeNode(1)
    it = BSTIterator(root)
    while it.hasNext():
        print it.next()