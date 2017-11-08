class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if not len(A):
            return 0
        current_pending = A[0]
        max_profit = 0
        for i in xrange(1, len(A)):
            if current_pending <= A[i]:
                max_profit += A[i] - current_pending
            current_pending = A[i]
        return max_profit


if __name__ == '__main__':
    print Solution().maxProfit([1, 6, 5, 9])

