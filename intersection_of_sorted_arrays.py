class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        a_pointer = 0
        b_pointer = 0
        result = []
        while a_pointer < len(A) and b_pointer < len(B):
            if A[a_pointer] == B[b_pointer]:
                result.append(A[a_pointer])
                a_pointer += 1
                b_pointer += 1
                continue
            if A[a_pointer] < B[b_pointer]:
                a_pointer += 1
            else:
                b_pointer += 1
        return result

