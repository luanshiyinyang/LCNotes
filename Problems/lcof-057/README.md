## 题目描述

输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

**示例 1：**
```
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
```
**示例 2：**
```
输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
```


## 题解思路

由于本题的数组是排好序的，可以很容易地想到双指针的思路，具体流程如下（正确性证明略去）。

1. **初始化**： 双指针 ii , jj 分别指向数组 numsnums 的左右两端 （俗称对撞双指针）。
2. **循环搜索**： 当双指针相遇时跳出；
    - 计算和 `s = nums[i] + nums[j]`；
    - 若`s > target` ，则指针`j`向左移动，即执行`j = j - 1`；
    - 若`s < target` ，则指针`i`向右移动，即执行`i = i + 1` ；
    - 若 `s = target`，立即返回数组 `[nums[i], nums[j]]`；
3. 返回空数组，代表无和为`target`的数字组合。

代码如下，也可见于[solve.py](./solve.py)。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                return nums[i], nums[j]
        return []
```

上述解法的时间复杂度为$O(N)$（$N$为数组`nums`的长度；双指针共同线性遍历整个数组），空间复杂度为$O(1)$：变量 `i`, `j` 使用常数大小的额外空间。