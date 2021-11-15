## 题目描述

给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

![](https://i.loli.net/2021/11/15/woTE6JaenfZMRXQ.gif)

**示例1：**

```
输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
```

**示例2：**

```
输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

**示例3：**

```
输入: numRows = 1
输出: [[1]]
```

## 题解思路

动态规划的思路， $dp[row][col]$ 表示第 $row$ 行 第 $col$ 列的值，其状态转移方程为： $dp[row][col]=dp[row-1][col-1]+dp[row-1][col]$ 。

时间复杂度为 $O(n^2)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> res(numRows);
        for (int i = 0; i < numRows; i++) {
            res[i].resize(i + 1);
            res[i][0] = 1;
            res[i][i] = 1;
            for (int j = 1; j < i; j++) {
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j];
            }
        }
        return res;
    }
};

```
