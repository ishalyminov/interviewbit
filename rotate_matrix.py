class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        if len(A) == 1:
            return A
        for i_start in xrange(len(A) - 1):
            for j_start in xrange(i_start, len(A) - i_start - 1):
                i = i_start
                j = j_start
                new_i = -1
                new_j = -1
                while new_i != i_start or new_j != j_start:
                    new_i = j
                    new_j = len(A) - i - 1
                    A[i_start][j_start], A[new_i][new_j] = A[new_i][new_j], A[i_start][j_start]
                    i = new_i
                    j = new_j
        return A

if __name__ == '__main__':
    print Solution().rotate([[1, 2], [3, 4]])