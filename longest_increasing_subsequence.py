class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        q = [0 for _ in xrange(len(A))]
        q[0] = 1
        for i in xrange(1, len(A)):
            for j in xrange(i):
                if A[j] < A[i]:
                    q[i] = max(q[i], q[j])
            q[i] += 1
        return max(q)
