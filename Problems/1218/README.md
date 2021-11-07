## 题目描述

给你一个整数数组 arr 和一个整数 difference，请你找出并返回 arr 中最长等差子序列的长度，该子序列中相邻元素之间的差等于 difference 。

**子序列** 是指在不改变其余元素顺序的情况下，通过删除一些元素或不删除任何元素而从 arr 派生出来的序列。

**示例1：**

```
输入：arr = [1,2,3,4], difference = 1
输出：4
解释：最长的等差子序列是 [1,2,3,4]。
```

**示例2：**

```
输入：arr = [1,3,5,7], difference = 1
输出：1
解释：最长的等差子序列是任意单个元素。
```

**示例3：**

```
输入：arr = [1,5,7,8,5,3,4,2,1], difference = -2
输出：4
解释：最长的等差子序列是 [7,5,3,1]。
```

## 题解思路

这题用动态规划还是挺巧妙的。

每个数字对应的等差子序列设为 $dp[i]$ ，则状态转移方程为： $dp[i] = dp[i - difference] + 1$ 。最长的等差子序列即为所有 $dp[i]$ 的最大值。

由于 $-10^4 \leq i \leq 10^4$ ， $i$ 可能为负数， $dp[i]$ 也可能不连续，可用哈希表来 $dp[i]$ 。

时间复杂度为 $O(n)$ ，空间复杂度为 $O(n)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution {
public:
    bool isPerfectSquare(int num) {
        int left = 0, right = num;
        while(right >= left){
            int half = left + (right - left) / 2;
            long square = (long)half * half;
            if(square < num){
                left = half + 1;
            }
            else if(square > num){
                right = half - 1;
            }
            else{
                return true;
            }
        }
        return false;
    }
};

```
