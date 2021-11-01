class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1):
            dp[i][i+1] = 0 if s[i] == s[i+1] else 1
        
        for i in range(2, n):
            for j in range(n-i):
                if s[j] == s[j+i]:
                    dp[j][j+i] = dp[j+1][j+i-1]
                else:
                    dp[j][j+i] = min(dp[j+1][j+i], dp[j][j+i-1]) + 1
        return dp[0][n-1]