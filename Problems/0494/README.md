## 题目描述
给你一个整数数组`nums`和一个整数`target`。

向数组中的每个整数前添加'`+`'或'`-`'，然后串联起所有整数，可以构造一个表达式：

例如，`nums = [2, 1]`，可以在`2`之前添加'`+`'，在`1`之前添加'`-`'，然后串联起来得到表达式"`+2-1`"。
返回可以通过上述方法构造的运算结果等于`target`的不同表达式的数目。

**示例：**
```
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
```

## 题解思路
直观上看题目似乎并不是背包问题，所以需要一定的转换。我们首先假设`total`为数组所有数组总和，`P`为前面是加号的所有数组总和，`N`为前面是减号的所有数字总和：
$$
P + N = total \\
P - N = target
$$
所以我们得到$N = (total - target) / 2$。也就是说，我们要从数组`nums`中找寻若干种组合，使得其和为`N`，最终的组合数量便是需要的答案。显而易见，当$total - target$为奇数的时候，无法除以2，所以很显然这种情况应该返回0，然后套01背包问题的模板即可。

代码如下，也可见[solve.py](./solve.py)。
```python
class Solution:
    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
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
```

## 优化思路
依旧是01背包问题中的空间优化，代码如下，也可见[solve.py](./solve.py)。
```python
class Solution:
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
```