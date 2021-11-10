## 题目描述

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

**示例1：**

```
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
```

**示例2：**

```
输入：nums = [1]
输出：1
```

**示例3：**

```
输入：nums = [0]
输出：0
```

**示例4：**

```
输入：nums = [-1]
输出：-1
```

**示例5：**

```
输入：nums = [-100000]
输出：-100000
```

## 题解思路

动态规划的思路，其状态转移方程为： $dp[i + 1] = max(x, dp[i] + x)$ 。

时间复杂度为 $O(n)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int pre = 0, res = INT_MIN;
        for(int num : nums){
            pre = max(pre + num, num);
            res = max(res, pre);
        }
        return res;
    }
};

```
