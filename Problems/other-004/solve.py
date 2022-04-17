class Solution():
    def count_valid_seq(self, s, k=9):
        MOD = int(1e9 + 7)
        n = len(s)
        dp = [[0] * k for _ in range(n)]
        dp[0][int(s[0]) % k] = 1
        for i in range(1, n):
            m = int(s[i]) % k
            dp[i][m] = dp[i][m] + 1
            for j in range(k):
                dp[i][j] += dp[i-1][j] + dp[i-1][(j+k-m) % k]
        return dp[-1][0] % MOD


print(Solution().count_valid_seq("0123"))