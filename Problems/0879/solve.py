class Solution:
    def profitableSchemes1(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        length = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(length + 1)]
        dp[0][0][0] = 1
        for i in range(1, length + 1):
            g, p = group[i - 1], profit[i - 1]
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    if j < g:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - g][max(0, k - p)]) % (10**9 + 7)
        ans = sum(dp[length][j][minProfit] for j in range(n + 1))
        return ans % (10**9 + 7)
    
    def profitableSchemes2(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        for i in range(0, n + 1):
            dp[i][0] = 1
        for earn, members in zip(profit, group):
            for j in range(n, members - 1, -1):
                for k in range(minProfit, -1, -1):
                    dp[j][k] = (dp[j][k] + dp[j - members][max(0, k - earn)]) % (10**9 + 7)
        return dp[n][minProfit]