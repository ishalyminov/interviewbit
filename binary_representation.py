class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        if not A:
            return '0'
        result = ''
        while A:
            next_digit = A % 2
            result = str(next_digit) + result
            A >>= 1
        return result

