## 题目描述

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

**示例：**

```
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
```

## 题解思路

双指针的思路，指针一指向排列好的数组的后一个数字（即指针前面均为非零数字），指针二遍历数组，若指针二指向非零数字，则交换两个指针对应的数字，指针一指向下一个数字。

时间复杂度为 $O(n)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int left = 0, right = 0;
        while(right < nums.size()){
            if (nums[right]) {
                swap(nums[left], nums[right]);
                left++;
            }
            right++;
        }
    }
};

```
