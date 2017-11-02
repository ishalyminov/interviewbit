class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        result = set([])

        self.permuteRegion(A, 0, len(A), result)
        return list(result)

    def permuteRegion(self, A, begin, end, result):
        if begin == end:
            return
        for i in xrange(begin, end):
            A[begin], A[i] = A[i], A[begin]
            result.add(tuple(A))
            self.permuteRegion(A, begin + 1, end, result)
            A[begin], A[i] = A[i], A[begin]

if __name__ == '__main__':
    print Solution().permute([1, 2, 3])