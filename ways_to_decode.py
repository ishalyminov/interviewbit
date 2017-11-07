class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        import string
        dictionary = {
            str(index + 1): letter for index, letter in enumerate(string.uppercase)
        }
        table = [0 for _ in xrange(len(A) + 1)]
        table[0] = 1
        for index in xrange(1, len(A) + 1):
            a_index = index - 1
            if A[a_index] in dictionary:
                table[index] = table[index - 1]
            if a_index == 0:
                continue
            if A[a_index - 1: a_index + 1] in dictionary:
                table[index] += table[index - 2]
        return table[-1]



if __name__ == '__main__':
    print Solution().numDecodings('10')
