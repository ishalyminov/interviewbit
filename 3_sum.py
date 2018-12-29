class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        from collections import defaultdict
        if len(A) < 3:
            return sum(A)

        A = sorted(A)
        closest = sum(A[:3])

        for ind, elem in enumerate(A):
            ind_left, ind_right = 0, len(A) - 1
            while ind_left < ind_right:
                if ind_left == ind:
                    ind_left += 1
                    continue
                if ind_right == ind:
                    ind_right -= 1
                    continue
                candidate = elem + A[ind_left] + A[ind_right]
                if abs(B - candidate) < abs(B - closest):
                    closest = candidate
                if candidate == B:
                    return candidate
                if candidate - B < 0:
                    ind_left += 1
                else:
                    ind_right -= 1

        return closest

# print Solution().threeSumClosest([-10, -10, -10], -5)
