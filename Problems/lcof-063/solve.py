class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices: return 0
        ans, mmin = 0, prices[0]
        for i in range(1, len(prices)):
            temp = prices[i] - mmin
            if temp > ans:
                ans = temp
            if prices[i] < mmin:
                mmin = prices[i]
        return ans