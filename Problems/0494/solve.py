class Solution:
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < target: return 0
        if (total - target) % 2 == 1: return 0
        neg = (total - target) // 2
        n = len(nums)
        dp = [[0] * (neg + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(neg + 1):
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
        return dp[n][neg]
    
    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < target: return 0
        if (total - target) % 2 == 1: return 0
        neg = (total - target) // 2
        n = len(nums)
        dp = [0] * (neg + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(neg, -1, -1):
                if nums[i - 1] <= j:
                    dp[j] += dp[j - nums[i - 1]]
        return dp[-1]