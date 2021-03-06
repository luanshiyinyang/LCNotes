## 题目描述

给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

**示例 1:**

![](https://s2.loli.net/2022/03/30/ktbvSziyKwuXFIB.jpg)

```
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
```

**示例 2：**

![](https://s2.loli.net/2022/03/30/m8SsR53NYhowukp.jpg)

```
输入： heights = [2,4]
输出： 4
```

## 题解思路

柱子彼此相邻，宽度均为1，高度各不相同。对于当前考察的柱子而言，它所能勾勒出的矩形面积是由其左边柱子和右边柱子的高度共同决定的。

若其左边柱子的高度大于等于当前柱子的高度，则可以向左扩张，知道左边柱子高度小于当前柱子高度或者左边再无柱子；右侧同理。此时，可以计算出以当前柱子高度为高，左右柱子距离为宽的矩形面积。

我们首先想到的当然是暴力解法，即遍历每个柱子，分别向左和向右扩张边界，直到边界索引对应的柱子高度小于当前考察的柱子的高度。

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        res = 0

        for i in range(size):
            left = i
            cur_height = heights[i]
            while left > 0 and heights[left - 1] >= cur_height:
                left -= 1

            right = i
            while right < size - 1 and heights[right + 1] >= cur_height:
                right += 1

            max_width = right - left + 1
            res = max(res, max_width * cur_height)
        return res
```

遗憾的是，这题若采用暴力解法，是必然超时的。

## 优化思路

我们来想想有什么优化的思路呢？我们注意到，在我们暴力解法中，对于当前考察的柱子，需要分别向左和向右遍历，以确定其是否可以继续扩张从而定出边界。那么，有没有方法在一次遍历中确定左右边界呢？

其实可以，我们以第一个示例`[2, 1, 5, 6, 2, 3]`来说。

- 在考察第一个柱子（值为2）时，由于不知道其是否可以继续向右扩张（左边界是可以确定的），所以将其记录下来，然后考察下一个柱子。
- 在考察到第二个柱子（值为1）时，我们发现它的值小于之前记录的柱子高度2，因此，这时其实可以确定第一个柱子所能勾勒出的矩形的面积。在确定完它的面积后，我们可以从记录中将第一个柱子删除。由于第二个柱子无法确定边界，我们将其记录下来。
- 然后，考虑第三个柱子（值为5），这时这个柱子的高度大于第二个柱子的高度，因此无法确定矩形，我们继续将其记录。
- 继续考察第四个柱子（值为6），它的高度大于记录中的两个柱子（值为1和5）的高度。因此，这三个柱子所能构成的矩形依然不能确定，将当前柱子继续记录。此时记录里的柱子值为`[1, 5, 6]`。
- 然后考察第五个柱子，其高度为2，小于之前一个柱子的高度6，因此，可以确定以6为高的柱子所能勾勒出的矩形面积。具体而言，由于之前记录的柱子高度是递增的，因此其左侧边界必为记录中的上一个位置的柱子。同时，由于当前考察的柱子比记录最后一个小，因此当前柱子就是其右侧边界。因此，可以确定面积，确定后从记录中删去它即可。
- 继续处理记录中的其他柱子。

可以发现，我们记录暂时不能确定左右边界的柱子时，是从左往右放入记录表中的；当可以确定边界时，是从右往左移除记录表的，这个特性符合栈，并且由于栈中元素递增，因此这是一个标准的单调栈。

求解思路如下：
- 在给定数组左右两侧添加高度为0的柱子以方便边界处理；
- 自左向右遍历数组元素：
  - 若是栈为空或者当前考察的新元素比栈顶元素值大，表明以栈顶元素为高的矩形面积暂时无法确定，将当前考察的元素入栈。因此，栈中元素是递增的。
  - 如果栈不空且当前考察的元素值比栈顶元素小，表明以栈顶元素值为高的矩形面积此时可以确定。矩形的高就是栈顶元素值，右边界就是当前考察的新元素，左边界是栈顶元素的前一个元素，由此可以作差减一得到矩形的宽。
  - 需要注意，当栈顶元素出栈后需要继续判断当前考察的元素是否小于新的栈顶元素，如果满足，则继续弹栈处理，直到当前考察的元素值大于栈顶元素，考察的元素入栈。
由于宽度是索引的差，因此栈中存放的是数组的索引。

具体代码如下，也可见于[solve.py](./solve.py)。

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        res = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                tmp = stack.pop()
                res = max(res, heights[tmp] * (i - stack[-1] - 1))
            stack.append(i)
        return res
```