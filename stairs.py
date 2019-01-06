class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        self.dp = [-1 for _ in range(A + 2)]
        self.dp[0] = 0
        self.dp[1] = 1

        return self.waysToClimb(A + 1)

    def waysToClimb(self, number):
        number = max(number, 0)
        if self.dp[number] != -1:
            return self.dp[number]

        self.dp[number] = self.waysToClimb(number - 1) + self.waysToClimb(number - 2)
        return self.dp[number]