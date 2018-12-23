class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        import math
        result = set([])
        for i in xrange(1, int(math.sqrt(A)) + 1):
            if A % i == 0:
                result.add(i)
                result.add(A // i)
        return sorted(result)

