## 题目描述

给你一个按 **非递减顺序** 排序的整数数组 nums，返回 **每个数字的平方** 组成的新数组，要求也按 **非递减顺序** 排序。

**示例1：**

```
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
```

**示例2：**

```
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]
```

## 题解思路

双指针的思路，一个指针指向开头，另一个指针指向结尾。比较两指针对应的值的平方，将较大的值放入结果并移动相应的指针。

时间复杂度为 $O(n)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int i = 0, j = nums.size() - 1, pos = nums.size() - 1;
        vector<int> res(nums.size());
        while(i <= j && pos >= 0){
            if (nums[i] * nums[i] >= nums[j] * nums[j]){
                res[pos--] = nums[i] * nums[i];
                i++;
            } else {
                res[pos--] = nums[j] * nums[j];
                j--;
            }
        }
        return res;
    }
};

```
