class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        row = [0 for _ in xrange(len(A[0]))]
        prev_row = [0 for _ in xrange(len(A[0]))]
        row[0] = int(A[0][0] == 0)
        for i in xrange(len(A)):
            for j in xrange(len(row)):
                if A[i][j] == 1:
                    continue
                row[j] += prev_row[j]
                if 0 < j:
                    row[j] += row[j - 1]
            prev_row = row
            row = [0 for _ in xrange(len(A[0]))]
        return prev_row[len(A[0]) - 1]


if __name__ == '__main__':
    print Solution().uniquePathsWithObstacles([
  [0,1]
])
