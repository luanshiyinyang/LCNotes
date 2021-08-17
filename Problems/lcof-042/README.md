## 题目描述

输入一个整型数组`nums`，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O(n)。

```
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```

## 题解思路


本题存在多种解法，包括暴力遍历、分治、动态规划等，其复杂度如下表所示，可自行推导。

|解法|时间复杂度|空间复杂度|
|:---:|:---:|:---:|
|暴力搜索| $O(N^2)$ | $O(1)$|
|分治|$O(NlogN)$|$O(NlogN)$|
|动态规划|$O(N)$|$O(1)|

下面描述如何想到这个思路，其实很容易想到，前i个数字的最大和子数组和其实与前i-1个数字的最大和子数组存在递推关系。

**状态定义**

我们不妨定义规划列表`dp`，其中`dp[i]`表示以`nums[i]`为结尾的连续子数组最大和（这里包含`nums[i]`是为了保证连续性，即**连续子数组**这一要求）。

**初始状态**

显然有`dp[0] = nums[0]`。

**状态转移方程**

状态转移方程的定义是`dp[i-1]`与`dp[i]`的关系，这个关系其实很简单，也就是说`dp[i-1]`若小于等于0，那么加上它其实对`dp[i]`的贡献为负数，因此此时选择`nums[i]`要比`dp[i-1]+nums[i]`合适，具体如下式。

$$
dp[i] = max(dp[i-1]+nums[i], nums[i])
$$

**返回值**

根据本体的`dp`定义，最优解其实是`dp`数组的最大值。

**复杂度优化**

由于`dp[i]`只与`dp[i-1]`和`nums[i]`有关系，因此可以将原数组`nums`用作`dp`列表，也就是直接在`nums`上修改即可。因此可以省去`dp`列表使用的额外空间，因此空间复杂度从$O(N)$降至$O(1)$。而时间复杂度方面，线性遍历`nums`是必须的，因此为$O(N)$。


原始版和优化版完整代码如下，也可见[solve.py](./solve.py)。

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)
```

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)
```