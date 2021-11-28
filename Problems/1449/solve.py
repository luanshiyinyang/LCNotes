class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [float("-inf")] * (target + 1)
        dp[0] = 0
        for c in cost:
            for i in range(c, target+1):
                dp[i] = max(dp[i], dp[i-c] + 1)
        
        if dp[target] < 0:
            return "0"
        
        ans = []
        j = target
        for i in range(8, -1, -1):
            c = cost[i]
            while j >= c and dp[j] == dp[j-c] + 1:
                j -= c
                ans.append(str(i+1))
        
        return "".join(ans)