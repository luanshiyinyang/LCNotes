## 题目描述

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

* 每行中的整数从左到右按升序排列。
* 每行的第一个整数大于前一行的最后一个整数。

**示例1：**

![0074_1](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)
```
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
```

**示例2：**

![0074_2](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/25/mat2.jpg)
```
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
```

## 题解思路

两次二分查找法的思路：

* 由于每行的第一个整数大于前一行的最后一个整数，可先用二分查找法找 $target$ 可能所在的行；
* 在所确定行中用二分查找法找 $target$ 所在的位置。

时间复杂度为 $O(\log mn)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution
{
public:
    bool searchMatrix(vector<vector<int>> &matrix, int target)
    {
        int m = matrix.size(), n = matrix[0].size(), rowLeft = 0, rowRight = m - 1, mid = 0, row = mid;
        while (rowLeft <= rowRight)
        {
            mid = rowLeft + (rowRight - rowLeft) / 2;
            if (matrix[mid][0] <= target && matrix[mid][n - 1] >= target)
            {
                break;
            }
            if (matrix[mid][0] > target)
            {
                rowRight = mid - 1;
            }
            else if (matrix[mid][n - 1] < target)
            {
                rowLeft = mid + 1;
            }
        }
        row = mid;
        int colLeft = 0, colRight = n - 1;
        while (colLeft <= colRight)
        {
            int mid = colLeft + (colRight - colLeft) / 2;
            if (matrix[row][mid] == target)
            {
                return true;
            }
            if (matrix[row][mid] > target)
            {
                colRight = mid - 1;
            }
            else if (matrix[row][mid] < target)
            {
                colLeft = mid + 1;
            }
        }
        return false;
    }
};

```
