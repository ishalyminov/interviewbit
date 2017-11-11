# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        result_root = ListNode(0)
        result_head = result_root
        remainder = 0
        while A is not None or B is not None:
            a_val = A.val if A else 0
            b_val = B.val if B else 0
            next_digit = a_val + b_val + remainder
            result_head.next = ListNode(next_digit % 10)
            remainder = next_digit / 10
            A = A.next if A else A
            B = B.next if B else B
            result_head = result_head.next
        if remainder:
            result_head.next = ListNode(remainder)
        return result_root.next


if __name__ == '__main__':
    num1 = ListNode(9)
    num1.next = ListNode(9)
    num1.next.next = ListNode(1)

    num2 = ListNode(1)
    #num2.next = ListNode(6)
    #num2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(num1, num2)
    print result
