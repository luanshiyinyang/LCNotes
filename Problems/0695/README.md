## 题目描述

给你一个大小为 m x n 的二进制矩阵 grid 。

岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 **水平或者竖直的四个方向上** 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

岛屿的面积是岛上值为 1 的单元格的数目。

计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。

**示例1：**

![695](https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg)
```
输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
输出：6
解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
```

**示例2：**

```
输入：grid = [[0,0,0,0,0,0,0,0]]
输出：0
```

## 题解思路

深度优先搜索的思路：

* 遍历数组，若值为 1 ，深度优先搜索该岛屿，得到该岛屿的面积，并将该岛屿的值置为 0，以免重复遍历该岛，保证每个元素只被遍历一次；
* 获取所有岛屿的值，从而得到面积最大的岛屿。

时间复杂度为 $O(n^2)$ ，空间复杂度为 $O(n^2)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution
{
public:
    const int dx[4] = {1, 0, 0, -1};
    const int dy[4] = {0, 1, -1, 0};
    int maxAreaOfIsland(vector<vector<int>> &grid)
    {
        int res = 0;
        for (int x = 0; x < grid.size(); x++)
        {
            for (int y = 0; y < grid[0].size(); y++)
            {
                res = max(res, dfs(grid, x, y));
            }
        }
        return res;
    }

    int dfs(vector<vector<int>> &grid, int x, int y)
    {
        int res = 0;
        if (grid[x][y] == 1)
        {
            grid[x][y] = 0;
            res++;
            for (int i = 0; i < 4; i++)
            {
                int mx = x + dx[i], my = y + dy[i];
                if (mx >= 0 && my >= 0 && mx < grid.size() && my < grid[0].size())
                {
                    res += dfs(grid, mx, my);
                }
            }
        }
        return res;
    }
};

```
