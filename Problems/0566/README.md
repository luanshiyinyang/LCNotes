## 题目描述

在 MATLAB 中，有一个非常有用的函数 reshape ，它可以将一个 m x n 矩阵重塑为另一个大小不同（r x c）的新矩阵，但保留其原始数据。

给你一个由二维数组 mat 表示的 m x n 矩阵，以及两个正整数 r 和 c ，分别表示想要的重构的矩阵的行数和列数。

重构后的矩阵需要将原始矩阵的所有元素以相同的 **行遍历顺序** 填充。

如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

**示例1：**

![](https://i.loli.net/2021/11/15/UPueK5W1Aqo2mtF.jpg)

```
输入：mat = [[1,2],[3,4]], r = 1, c = 4
输出：[[1,2,3,4]]
```

**示例2：**

![](https://i.loli.net/2021/11/15/ErBoFQD3pARKYGs.jpg)

```
输入：mat = [[1,2],[3,4]], r = 2, c = 4
输出：[[1,2],[3,4]]
```

## 题解思路

二维数组和一维数组的相互转换， $mat[i / n][i \% n] = mat[i]$ 。

时间复杂度为 $O(m * n)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int m = mat.size(), n = mat[0].size();
        vector<vector<int>> res(r);
        if (m * n != r * c){
            return mat;
        }
        for (int i = 0; i < m * n; i++) {
            if (i % c == 0) {
                res[i / c].resize(c);
            }
            res[i / c][i % c] = mat[i / n][i % n];
        }
        return res;
    }
};

```
