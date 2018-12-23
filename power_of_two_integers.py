class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A < 2:
            return 1
        for factor in self.allFactors(A):
            if self.isPowerOf(A, factor):
                return int(True)
        return int(False)

    def isPowerOf(self, A, i):
        while i <= A:
            remainder = A % i
            if remainder:
                return False
            A = A // i
            if A == 1:
                return True
        return False

    def allFactors(self, A):
        import math
        result_remainder = set([])
        for i in xrange(2, int(math.sqrt(A)) + 1):
            if A % i == 0:
                yield i
                result_remainder.add(A // i)
        for i in sorted(result_remainder):
            yield i

