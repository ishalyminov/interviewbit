class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        self.best, self.candidate = [], []
        self.best_sum, self.candidate_sum = 0, 0
        for elem in A:
            if elem < 0:
                self.update_best()
                continue
            else:
                self.candidate.append(elem)
                self.candidate_sum += elem
        self.update_best()
        return ' '.join([str(elem) for elem in self.best]) + ' '

    def update_best(self):
        if self.best_sum < self.candidate_sum:
            self.best_sum = self.candidate_sum
            self.best = self.candidate
        elif self.best_sum == self.candidate_sum and len(self.best) < len(self.candidate):
            self.best = self.candidate
        self.candidate_sum = 0
        self.candidate = []

