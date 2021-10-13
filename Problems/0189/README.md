## 题目描述

给定一个数组，将数组中的元素向右移动 `k` 个位置，其中 `k` 是非负数。

**示例1**：
```
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
```

**示例2**：
```
输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
```

## 题解思路

我们知道，对位置i而言，它对应的交换位置其实是$x=(i+k) mod n$。但是我们不能将先前位置直接替换到目标位置，因为这样会造成被放置元素位置原来的值因为覆盖而消失，我们可以将其保存在临时的temp元素中。下面我们详述算法的流程。

从位置0开始，令temp=nums[0]。根据规则，位置0的元素会被放置在$(0+k) mod n$的位置，令$x=(0+k) mod n$，此时交换temp和nums[x]就完成了x位置的更新。然后将x位置作为新的初始位置，交换temp和nums[$(x+k) mod n$]，完成下一次更新，直到回到初始位置0。

显然，上述过程（称为第一趟）回到初始位置之后，并没有遍历到所有的元素，因此需要从上一趟的初始元素的后一个位置开始新的一趟处理。那么所有趟要何时才能结束呢，其实很简单，通过计数器记录进行交换的元素数目，当计数器到达nums元素总数时即可停止循环。

以下面的案例为例，其两趟处理如下图。

```
nums = [1, 2, 3, 4, 5, 6]
k = 2
```

![](https://i.loli.net/2021/10/13/3wvnXT2EIdt7ZR9.png)


代码如下，也可见于[solve.py](./solve.py)。

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count = 0
        start = 0
        while count < n:

            current = start
            pre = nums[current]
            
            while True:
                next_index = (current + k) % n
                temp = nums[next_index]
                nums[next_index] = pre
                current = next_index
                pre = temp
                count += 1
                if start == current:
                    break
                
            start += 1
```

显然，上述解法的时间复杂度为$O(n)$，空间复杂度为$O(1)$。