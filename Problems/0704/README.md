## 题目描述

给定一个`n`个元素有序的（升序）整型数组`nums`和一个目标值`target`，写一个函数搜索`nums`中的`target`，如果目标值存在返回下标，否则返回 `-1`。

**示例 1:**

```
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
```

**示例 2:**

```
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
```

## 题解思路

这是二分查找最经典的一题，题目名就叫“二分查找”，

二分查找的做法是，定义查找的范围`[left,right]`，初始查找范围是整个数组。每次取查找范围的中点`mid`，比较`nums[mid]` 和`target`的大小，如果相等则`mid`即为要寻找的下标，如果不相等则根据`nums[mid]`和`target` 的大小关系将查找范围缩小一半。

由于每次查找都会将查找范围缩小一半，因此二分查找的时间复杂度是`O(logn)`，其中 `n`是数组的长度。

对本题而言，在升序数组`nums`中寻找目标值`target`，对于特定下标`i`，比较`nums[i]`和`target`的大小：

- 若`nums[i] = `target`}，则下标`i`即为要寻找的下标；
- 若`nums[i]` > `target`，则`target`只可能在下标`i`的左侧；
- 若`nums[i]` < `target`，则`target`只可能在下标`i`的右侧。

代码如下所示，也可见于[solve.py](./solve.py)。

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            num = nums[mid]
            if num == target:
                return mid
            elif target < num:
                right = mid - 1
            else:
                left = mid + 1
        return -1
```

上述解法的时间复杂度为$O(logn)$，空间复杂度为$O(1)$，$n$为数组长度。