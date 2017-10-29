class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        result = A[0]
        prefix = []
        prefix_sum = 0
        for element in A:
            if prefix_sum < 0:
                prefix = []
                prefix_sum = 0
            prefix.append(element)
            prefix_sum += element
            result = max(result, prefix_sum)
        return result


if __name__ == '__main__':
    print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
