## 题目描述

给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

**示例1：**

```
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
```

**示例2：**

```
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
```

## 题解思路

由于是升序有序数组，取数组中间的一个元素，若 $target$ 小于该值，则 $target$ 位置再该值之前，若大于，则在之后，递归地查找，直至找到 $target$ 。

时间复杂度为 $O(\log n)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int end = nums.size() - 1, start = 0, mid;
        while(start <= end){
            mid = start + (end - start) / 2;
            if(nums[mid] == target){
                return mid;
            } else if(nums[mid] > target){
                end = mid - 1;
            } else{
                start = mid + 1;
            }
        }
        return -1;
    }
};

```
