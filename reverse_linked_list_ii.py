# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, m, n):
        if not A or not A.next:
            return A
        root_node = ListNode(0)
        root_node.next = A
        counter = 1
        before_list_patch = root_node
        list_patch_begin = None
        list_patch_end = None
        after_list_patch = None
        current_node = A
        while current_node is not None:
            next_node = current_node.next
            if counter == m - 1:
                before_list_patch = current_node
            if counter == n + 1:
                after_list_patch = current_node
            if m <= counter <= n:
                if not list_patch_end:
                    list_patch_end = current_node
                if list_patch_begin:
                    current_node.next = list_patch_begin
                list_patch_begin = current_node
            current_node = next_node
            counter += 1
        before_list_patch.next = list_patch_begin
        list_patch_end.next = after_list_patch
        return root_node.next


if __name__ == '__main__':
    l = [ListNode(1), ListNode(2), ListNode(3)]
    for i in xrange(len(l) - 1):
        l[i].next = l[i + 1]
    print Solution().reverseBetween(l[0], 1, 2)
