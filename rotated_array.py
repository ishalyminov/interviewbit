class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        return self.findMinOnInterval(A, 0, len(A))

    def findMinOnInterval(self, A, begin, end):
        if self.isSortedOnRegion(A, begin, end):
            return A[begin]
        pivot = (begin + end) / 2
        if self.isSortedOnRegion(A, begin, pivot):
            return min(A[begin], self.findMinOnInterval(A, pivot, len(A)))
        else:
            return min(A[pivot], self.findMinOnInterval(A, begin, pivot))
        return a_min

    def isSortedOnRegion(self, A, begin, end):
        a_min, a_max = A[begin], A[end - 1]
        return a_min <= a_max


if __name__ == '__main__':
    print Solution().findMin([4, 5, 6, 7, 8, 9, 1, 2, 3])