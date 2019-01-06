class Solution:
    # @param A : string
    # @return an integer
    def cnttrue(self, A):
        from collections import defaultdict

        self.operands, self.operators = [], []
        self.false = defaultdict(lambda: -1)
        self.true = defaultdict(lambda: -1)

        for elem in A:
            if elem in ['T', 'F']:
                index = len(self.operands)
                self.operands.append(elem == 'T')
                self.true[(index, index)] = int(elem == 'T')
                self.false[(index, index)] = int(elem == 'F')
            else:
                self.operators.append(elem)

        return int(self.cntTrueInInterval(0, len(self.operands) - 1)) % 1003

    def cntTrueInInterval(self, start, end):
        if end < start:
            return 0

        if self.true[(start, end)] != -1:
            return self.true[(start, end)]

        tmp = 0
        for index in range(start, end):
            if self.operators[index] == '&':
                tmp += self.cntTrueInInterval(start, index) * self.cntTrueInInterval(index + 1, end)
            elif self.operators[index] == '|':
                tmp += self.cntTrueInInterval(start, index) * self.cntTrueInInterval(index + 1, end) + \
                       self.cntTrueInInterval(start, index) * self.cntFalseInInterval(index + 1, end) + \
                       self.cntFalseInInterval(start, index) * self.cntTrueInInterval(index + 1, end)
            elif self.operators[index] == '^':
                tmp += \
                    self.cntTrueInInterval(start, index) * self.cntFalseInInterval(index + 1, end) + \
                    self.cntFalseInInterval(start, index) * self.cntTrueInInterval(index + 1, end)
        # print('Interval {}, {}: {}'.format(start, end, tmp))
        self.true[(start, end)] = tmp
        return self.true[(start, end)]

    def cntFalseInInterval(self, start, end):
        if end < start:
            return 0

        if self.false[(start, end)] != -1:
            return self.false[(start, end)]

        tmp = 0
        for index in range(start, end):
            if self.operators[index] == '&':
                tmp += \
                    self.cntFalseInInterval(start, index) * self.cntFalseInInterval(index + 1, end) + \
                    self.cntFalseInInterval(start, index) * self.cntTrueInInterval(index + 1, end) + \
                    self.cntTrueInInterval(start, index) * self.cntFalseInInterval(index + 1, end)
            elif self.operators[index] == '|':
                tmp += self.cntFalseInInterval(start, index) * self.cntFalseInInterval(index + 1, end)
            elif self.operators[index] == '^':
                tmp += \
                    self.cntTrueInInterval(start, index) * self.cntTrueInInterval(index + 1, end) + \
                    self.cntFalseInInterval(start, index) * self.cntFalseInInterval(index + 1, end)
        self.false[(start, end)] = tmp
        return self.false[(start, end)]


print(Solution().cnttrue("F|T"))