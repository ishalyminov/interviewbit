class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A) < 2:
            return 0
        left_min = [elem for elem in A]
        right_max = [elem for elem in A]
        profits_left = [0 for _ in xrange(len(A))]
        profits_right = [0 for _ in xrange(len(A))]

        for index in xrange(1, len(A)):
            left_min[index] = min(left_min[index - 1], A[index])
            profits_left[index] = max(profits_left[index - 1], A[index] - left_min[index])
        for index in xrange(len(A) - 2, -1 , -1):
            right_max[index] = max(right_max[index + 1], A[index])
            profits_right[index] = max(profits_right[index + 1], right_max[index] - A[index])
        profit = max([left + right
                   for left, right in zip(profits_left, profits_right)])
        return profit


if __name__ == '__main__':
    print Solution().maxProfit([1, 2, 3, 1, 2, 5])
