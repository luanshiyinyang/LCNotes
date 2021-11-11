## 题目描述

给定一个已按照 **非递减顺序排列**  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 **从 1 开始计数** ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。

你可以假设每个输入 **只对应唯一的答案** ，而且你 **不可以** 重复使用相同的元素。

**示例1：**

```
输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
```

**示例2：**

```
输入：numbers = [2,3,4], target = 6
输出：[1,3]
```

**示例3：**

```
输入：numbers = [-1,0], target = -1
输出：[1,2]
```

## 题解思路

双指针的思路，指针一指向数组开头，指针二指向数组末尾。若指针一指向数字与指针二指向数字的和大于 $target$ ，则指针一指向其后继，若指针一指向数字与指针二指向数字的和小于 $target$ ，则指针二指向其前驱，直至找到和等于 $target$ 的两个数字。

时间复杂度为 $O(n)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0, right = numbers.size() - 1;
        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum > target) {
                right--;
            } else if (sum < target) {
                left++;
            } else {
                return {left + 1, right + 1};
            }
        }
        return {};
    }
};

```
