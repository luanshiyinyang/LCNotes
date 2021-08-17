## 题目描述

找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例：

输入：
[2, 3, 1, 0, 2, 5, 3]

输出：2 或 3 

## 解题思路

由于题目中只需要输出任意一个重复的数字即可，所以一上来想到的方法就是遍历一边数组，遇到重复的便输出数字，停止遍历。为了判断一个数字是否重复，可以在一开始初始化一个列表来存储已经遍历的数字，若是遇到一个数字已经在列表中，则是重复数字。

完整代码如下，也可见[solve.py](./solve.py)。

```python
class Solution:
    def findRepeatNumber1(self, nums: List[int]) -> int:
        re = []
        for n in nums:
            if n in re:
                return n
            else:
                re.append(n)
        return -1
```

## 优化思路

其实如果用python写的话，可以代用set（无序不重复），亦或者利用python自带的sort函数进行排序，然后查看相邻数字是否有重复。

上面代码的执行结果为：

![](https://i.loli.net/2021/08/17/278rX4Iv39Eafox.png)

后来又想了个方法，执行结果是这样：

![](https://i.loli.net/2021/08/17/xcgfIsb9LthG7Bj.png)

思路是这样的：开始遍历数组，若下表`i`的值`nums[i]`与`i`不相同，就将位置`i`的数字放到与值相等的下标的位置`nums[nums[i]]`，一直到`i`与`nums[i]`相等，再遍历`i+1`位置。当在上述过程中遇到，将`nums[i]`放到下标为`nums[i]`的地方时，`nums[i]`和`nums[nums[i]]`相等，就说明找到了重复的数字，输出即可。

完整代码如下，也可见[solve.py](./solve.py)。

```python
class Solution:
    def findRepeatNumber2(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while i != nums[i]:
                temp = nums[i]
                if temp == nums[temp]:
                    return temp
                t = nums[temp]
                nums[temp] = temp
                nums[i] = t
```

