class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if not len(A):
            return 0
        min_prices = [x for x in A]
        profits = [0 for _ in xrange(len(A))]
        for index in xrange(1, len(A)):
            element = A[index]
            profits[index] = max(profits[index], element - min_prices[index - 1])
            min_prices[index] = min(min_prices[index - 1], element)
        return max(profits)


if __name__ == '__main__':
    print Solution().maxProfit([2, 1])