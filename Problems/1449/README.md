## 题目描述

给你一个整数数组 `cost` 和一个整数 `target` 。请你返回满足如下规则可以得到的**最大**整数：
- 给当前结果添加一个数位`（i + 1）`的成本为 `cost[i]` （`cost` 数组下标从 0 开始）。
- 总成本必须恰好等于 `target` 。
- 添加的数位中没有数字 0 。

由于答案可能会很大，请你以字符串形式返回。如果按照上述要求无法得到任何整数，请你返回"0"。

**示例 1：**

```
输入：cost = [4,3,2,5,6,7,2,5,5], target = 9
输出："7772"
解释：添加数位 '7' 的成本为 2 ，添加数位 '2' 的成本为 3 。所以 "7772" 的代价为 2*3+ 3*1 = 9 。 "977" 也是满足要求的数字，但 "7772" 是较大的数字。
 数字     成本
  1  ->   4
  2  ->   3
  3  ->   2
  4  ->   5
  5  ->   6
  6  ->   7
  7  ->   2
  8  ->   5
  9  ->   5
```

**示例 2：**

```
输入：cost = [7,6,5,5,5,6,8,7,8], target = 12
输出："85"
解释：添加数位 '8' 的成本是 7 ，添加数位 '5' 的成本是 5 。"85" 的成本为 7 + 5 = 12 。
```

**示例 3：**

```
输入：cost = [2,4,6,2,4,6,4,4,4], target = 5
输出："0"
解释：总成本是 target 的条件下，无法生成任何整数。
```

**示例 4：**

```
输入：cost = [6,10,15,40,40,40,40,40,40], target = 47
输出："32211"
```

## 题解思路

这道题理解起来其实挺复杂的，但是抽丝剥茧出来，其实题意如下：现在为1到9每个数字设置一个代价`cost[i]`，用一次这个数字会消耗对应的代价，从中挑出若干个数字拼接为一个整数，这个整数的代价刚好要等于`target`，求出满足这个条件的最大整数。

拿到这道题，看到题目结构，我们可以分析出来，这其实是一个完全背包的问题，但是求解的目标应该是什么呢？显然不是拼接成的整数值，这很难递推。考虑到，**如果两个整数位数不同，那么位数更多的整数必然大于位数小的整数**，所以，我们需要计算的其实是可以拼接成的整数的最大位数。 

因此，原始问题抽象为**恰好**装满背包容量为`target`，物品重量为`cost[i]`，物品价值为1的完全背包问题。

这里可以套用完全背包的模板求解，具体参考[博客](https://zhouchen.blog.csdn.net/article/details/120564709)。具体定义来看，声明二维数组dp，其中$dp[i+1][j]$表示使用前$i$个数位且花费总成本恰好为$j$时的最大位数，若花费总成本无法为$j$，则规定其为 $-\infty$。特别地，$dp[0][]$为不选任何数位的状态，因此除了$dp[0][0]$为$0$，其余$dp[0][j]$全为 $-\infty$。

最后，我们得到的`dp[9][target]`就是可以得到的整数的最大位数，若其小于$0$则说明无法得到满足要求的整数，返回"0"即可。否则，我们需要生成一个整数，其位数为`dp[9][target]`，这就需要反向查找DP表了，尽量选择大的数位即可。

具体状态压缩后的代码如下，也可见于[solve.py](./solve.py)。

```python
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
```

上述解法的时间复杂度：$O(n \cdot⋅target)$。其中$n$是数组`cost`的长度。空间复杂度$O(target)$。