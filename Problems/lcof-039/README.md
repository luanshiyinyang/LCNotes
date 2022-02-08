## 题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。你可以假设数组是非空的，并且给定的数组总是存在多数元素。

**示例：**
```
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
```

## 题解思路
这题并不是很困难的，最简单的方法有两种：一是遍历数组，对每个出现的数字计数，最后输出最多的那个数字；二是将数组排序，然后中位数便是众数，即是所求。这里介绍一个空间复杂度为$O(1)$的算法——Boyer-Moore 投票算法。

首先，Boyer-Moore算法的主要流程如下：
- 维护一个候选众数`candidate`和其出现的次数`count`，初始化时`candidate`可以为任意值，`count`为0；
- 遍历数组中所有元素，对于每一个`x`，在对`x`进行判断之前，如果`count`为`0`，那将`x`的值赋予`candidate`，随后对`x`进行判断：
  - 若$x == candidate$，`count`加一；
  - 若$x != candidate$，`count`减一；
- 在遍历结束后，`candidate`的值便为所求众数。

以数组`[7, 7, 5, 7, 5, 1 , 5, 7 , 5, 5, 7, 7 , 7, 7, 7, 7]`为例：
```
nums:      [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 7, 7, 7, 7]
candidate:  7, 7, 7, 7, 7, 7, 5, 5, 5, 5, 5, 5, 7, 7, 7, 7
count:      1, 2, 1, 2, 1, 0, 1, 0, 1, 2, 1, 0, 1, 2, 3, 4
```
由于我们在`count`等于`0`时，直接将下一个`x`赋给`count`，所以`count`一直为非负。假设，我们在一开始采用`true`和真正的众数进行绑定，代表众数出现的次数比非众数出现的次数多出了多少次，我们会得到以下数据：
```
count: 1, 2, 1, 2, 1, 0, 1, 0, 1, 2, 1, 0, 1, 2, 3, 4
true:  1  2  1  2  1  0  -1  0  -1 -2 -1  0   1  2  3  4
```
不难发现，`count`和`true`要么相等，要么互为相反数。
代码如下，也可见[solve.py](solve.py)。
```python
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count, candidate = 0, None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
```