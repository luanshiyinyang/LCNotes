class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        # 初始状态
        dp[0][0] = 0
        accu = 0
        for i in range(1, m+1):
            accu += ord(s1[i-1])
            dp[i][0] = accu
        accu = 0
        for j in range(1, n+1):
            accu += ord(s2[j-1])
            dp[0][j] = accu
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
        return dp[-1][-1]