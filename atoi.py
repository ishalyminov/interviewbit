class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        INT_MAX = (1 << 31) - 1
        INT_MIN = -1 << 31
        result = 0
        sign = 1
        for index, chr in enumerate(A):
            if chr in ['-', '+'] and index == 0:
                if chr == '-':
                    sign = -1
                continue
            if '0' <= chr <= '9':
                result = result * 10 + int(chr)
                if INT_MAX < result * sign:
                    return INT_MAX
                if result * sign < INT_MIN:
                    return INT_MIN
            else:
                break
        return result * sign

# print Solution().atoi('-88297 248252140B12 37239U4622733246I218 9 1303 44 A83793H3G2 1674443R591 4368 7 97')