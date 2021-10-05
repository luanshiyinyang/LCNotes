## 题目描述

给你一个 **只包含正整数** 的 **非空** 数组 `nums` 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

设计一个算法使得这 m 个子数组各自和的最大值最小。

**示例 1：**
```
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
```

**示例 2：**
```
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。
```

## 题解思路

这道题可以转换一下题目：给定一个只包含正整数的非空数组`nums`，判断是否可以从数组中选择一些数字，使得这些数字的和等于整个数组元素和的一半，此时这个问题变为一个01背包问题。不过，不同意01背包物品重量不能超过背包总容量，这里要求选取的数字的和**恰好等于**整个数组的元素和的一半。

因此我们可以考虑使用动态规划来解题，根据base case，我们不妨维护二维dp数组，其中`dp[i][j]`表示在前i个数（包括第i个）中选取若干个正整数（也可以0个），是否存在一种方案使得被选取的正整数的和恰好等于j。

显然，对于二维dp我们首先需要考虑两个边界，即行边界和列边界。因此有下面两个边界情况。
- 对于列边界，即任意的`dp[i][0]`表示不选取任何正整数，因此被选取的正整数和为0，因此`dp[i][0] = true`。
- 对于行边界，即`dp[0][j]`，此时只有正整数`nums[0]`被选择，只有当j为`nums[0]`的时候，`dp[0][j] = true`，其余均为false。

下面，考虑正常的递推，也就是`i>0`且`j>0`的情况，需要分下面两种情况。

- 若$j \ge nums[i]$，那么此时的`nums[i]`可选可不选，两种情况只要有一种为true即有`dp[i][j] = true`。
- 若$j < nums[i]$，那么`nums[i]`不能选，此时`dp[i][j]=dp[i-1][j]`。

最终的状态转移方程如下。

$$
d p[i][j]= \begin{cases}d p[i-1][j] \mid d p[i-1][j-\text { nums }[i]], & j \geq \text { nums }[i] \\ d p[i-1][j], & j<\text { nums }[i]\end{cases}
$$

不过，这里需要考虑几个特判的情况，否则无法通过所有用例。
- 如果数组长度n小于2，直接返回false；
- 如果数组的和sum是奇数，直接返回false；
- 如果数组的和sum是偶数，那么`sum//2`则为target，若数组最大元素max比target还大，则直接返回false。

最终的代码如下。也可见于[solve.py](./solve.py)。

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        total = sum(nums)
        max_num = max(nums)
        # 若总和不能二等分，则必然不能拆分两份
        if total % 2 != 0:
            return False
        else:
            target = total // 2
        if max_num > target:
            return False
        dp = [[False] * (target+1) for _ in range(n)]
        # 第一行和第一列的初始化
        for i in range(n):
            dp[i][0] = True
        dp[0][nums[0]] = True
        
        for i in range(1, n):
            for j in range(1, target+1):
                if j > nums[i]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n-1][target]
```

这段代码的空间复杂度为$O(n \times target)$，时间复杂度为$O(n  \times target)$。

## 优化思路

类似于01背包问题，上述解法空间消耗是可以优化的，我们发现其实我们每次更新dp数组只是利用了上一行的信息，因此这里可以利用状态压缩，将dp数组压缩为一维数组。

此时的状态转移方程如下，需要注意的是第二层的循环我们需要从大到小计算，因为如果我们从小到大更新 dp 值，那么在计算 `dp[j]` 值的时候，`dp[j−nums[i]]` 已经是被更新过的状态，不再是上一行的 dp 值。

$$
d p[j]=d p[j] \mid d p[j-\text { nums }[i]]
$$

代码如下。

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        if n < 2:
            return False
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        
        target = total // 2

        dp = [True] + [False] * target
        
        for i, num in enumerate(nums):
            for j in range(target, num-1, -1):
                dp[j] = dp[j] or dp[j-num]
        return dp[target]
```

此时时间复杂度依然是$O(n \times target)$，但是空间复杂度降低为了$O(target)$。