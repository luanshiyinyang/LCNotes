class Solution:
    def findMaxForm1(self, strs: List[str], m: int, n: int) -> int:
        k = len(strs)
        if m == 0 and n == 0: return 0
        dp = [[[False] * (n + 1) for _ in range(m + 1)] for __ in range(k + 1)]
        for s in range(k+1):
            dp[s][0][0] = 0
        for i in range(m+1):
            for j in range(n+1):
                dp[0][i][j] = 0
        for s in range(1, k+1):
            for i in range(m + 1):
                for j in range(n + 1):
                    nums0, nums1 = self.count(strs[s - 1])
                    if nums0 <= i and nums1 <= j:
                        dp[s][i][j] = max(dp[s - 1][i][j], dp[s - 1][i - nums0][j - nums1] + 1)
                    else:
                        dp[s][i][j] = dp[s - 1][i][j]
        return dp[k][m][n]

    def findMaxForm2(self, strs: List[str], m: int, n: int) -> int:
        k = len(strs)
        if m == 0 and n == 0: return 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        for s in range(1, k + 1):
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    nums0, nums1 = self.count(strs[s - 1])
                    if nums0 <= i and nums1 <= j:
                        dp[i][j] = max(dp[i][j], dp[i - nums0][j - nums1] + 1)
        return dp[m][n]

    def count(self, s):
        count0, count1 = 0, 0
        for ss in s:
            if ss == '0':
                count0 += 1
            elif ss == '1':
                count1 += 1
        return count0, count1