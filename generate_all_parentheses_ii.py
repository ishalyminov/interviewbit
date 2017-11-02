class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        result = set([])
        result.update(self.generateParenthesisImpl(A))
        return sorted(result)

    def generateParenthesisImpl(self, in_pairs_number):
        if in_pairs_number <= 0:
            return ['']
        result = []
        for i in xrange(0, in_pairs_number):
            for left_seq in self.generateParenthesisImpl(i):
                for right_seq in self.generateParenthesisImpl(in_pairs_number - i - 1):
                    result.append('(' + left_seq + ')' + right_seq)
        return result

if __name__ == '__main__':
    print Solution().generateParenthesis(4)