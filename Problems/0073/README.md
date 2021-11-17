## 题目描述

给定一个 m x n 的矩阵，如果一个元素为 **0** ，则将其所在行和列的所有元素都设为 **0** 。请使用 **原地** 算法。

**示例1：**

![0073_1](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)

```
输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]
```

**示例2：**

![0073_2](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)

```
输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

## 题解思路

用两个数组分别存放值为 0 的行和列，再将两个数组中所有的行和列的所有元素变为 0 。

时间复杂度为 $O(mn)$ ，空间复杂度为 $O(m+n)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution
{
public:
    void setZeroes(vector<vector<int>> &matrix)
    {
        unordered_set<int> rowSet, colSet;
        for (int i = 0; i < matrix.size(); i++)
        {
            for (int j = 0; j < matrix[0].size(); j++)
            {
                if (matrix[i][j] == 0)
                {
                    rowSet.insert(i);
                    colSet.insert(j);
                }
            }
        }
        for (int x : rowSet)
        {
            for (int i = 0; i < matrix[0].size(); i++)
            {
                matrix[x][i] = 0;
            }
        }
        for (int y : colSet)
        {
            for (int i = 0; i < matrix.size(); i++)
            {
                matrix[i][y] = 0;
            }
        }
    }
};

```
