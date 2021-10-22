## 题目描述

给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

**示例1：**

![](https://i.loli.net/2021/10/22/Kafj5hymp3xLPIW.png)

```
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
```

**示例2：**

```
输入：height = [4,2,0,3,2,5]
输出：9
```

## 题解思路

接雨水类型的题目在面试中还是比较常见的，首先对于本题，我们必须明确一个概念---**对于下标i，下雨后能到达的最大高度等于下标i两边的最大高度的最小值，下标i处能接的雨水量等于下标i处的水能到达的最大高度减去当前位置i的高度，即减去`height[i]`。**

因此，我们不妨定义两个指针`left`和`right`从左右两侧开始遍历数组，并用两个变量leftmax和rightmax来记录左侧的最大值和右侧的最大值。首先，left和right分别指向数组头和数组尾，left只能右移且right只能左移，当两个指针，没有相遇的时候，进行如下操作：

- 使用`height[left]`和`height[right]`的值更新leftmax和rightmax；
- 若`height[left] < height[right]`，则此时必有`leftmax<rightmax`（说明见下一段），下标left处能接的雨水量等于`leftmax-height[left]`，left右移；
- 若`height[left] >= height[right]`，则此时必有`leftmax >= rightmax`（说明见下一段），下标right处能接的雨水量等于`rightmax-height[right]`，right左移。

> 这里解释上面的两个“必有”，左指针右移的终止条件是找到比 rightmax 大的 leftmax，也就是说一旦左指针终止左移，此时的height[left] 一定是 leftmax，且大于 rightmax。同理，右指针左移的终止条件是找到比 leftmax 大的 rightmax，而此时的 height[right] 就是 rightmax。所以这里 height[left] < height[right] 中的 height[right] 就是当前的 rightmax，而 height[left] < height[right]（rightmax）意味着还没找到大于 rightmax 的 leftmax，所以 leftmax < rightmax。

代码如下，也可见于[solve.py](./solve.py)。

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftmax, rightmax = 0, 0
        count = 0
        while left < right:
            leftmax = max(height[left], leftmax)
            rightmax = max(height[right], rightmax)
            if height[left] < height[right]:
                count += (leftmax - height[left])
                left += 1
            else:
                count += (rightmax - height[right])
                right -= 1
        return count
```

上述解法的复杂度。时间复杂度：$O(n)$O，其中 $n$ 是数组 height 的长度。两个指针的移动总次数不超过 $n$。空间复杂度：$O(1)$，只需要使用常数的额外空间。