class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        from collections import defaultdict
        table = defaultdict(lambda: set([]))

        self.combinationSumStep(A, B, table)
        return sorted(table[B])

    def combinationSumStep(self, A, B, table):
        if B <= 0:
            return []
        for element in A:
            if B < element:
                continue
            elif B == element:
                table[B].add((element,))
            else:
                self.combinationSumStep(A, B - element, table)
                for combination in table[B - element]:
                    if element < combination[-1]:
                        continue
                    table[B].add(combination + (element,))


if __name__ == '__main__':
    print Solution().combinationSum([2, 3, 6, 7], 7)