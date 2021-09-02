## 题目描述
在`x`轴上有一个一维的花园。花园长度为`n`，从点`0`开始，到点`n`结束。

花园里总共有`n + 1`个水龙头，分别位于`[0, 1, ..., n]`。

给你一个整数`n`和一个长度为`n + 1`的整数数组`ranges`，其中`ranges[i]`（下标从`0`开始）表示：如果打开点`i`处的水龙头，可以灌溉的区域为`[i -  ranges[i], i + ranges[i]]`。

请你返回可以灌溉整个花园的最少水龙头数目。如果花园始终存在无法灌溉到的地方，请你返回`-1`。

**示例及示例绘图。**
```
n = 5, ranges = [3,4,1,1,0,0]
```
![](https://i.loli.net/2021/09/02/tH9Q1EyTvczqVYI.png)

## 解题思路
其实这是较为经典的线段覆盖问题，只不过用了一个花园浇水的故事。简单了说就是：有若干条线段，选用最少数量的线段，覆盖`[0, n]`这个区域。比较容易理解的方法是贪心算法：首先通过题目的输入，得到所有的线段；初始化一个变量`left`，记录尚未被覆盖的区域的左端点，开始的时候为`0`；当`left`大于右端点`n`时停止循环，每一次循环，找到所有线段中左端点小于`left`的最长的一条线段，选用该线段进行覆盖，`left`更新为此线段的右端点；若当`left`依旧小于`n`，却无法找到满足左端点小于`left`的可选择线段，则表明这些线段无法覆盖区间`[0, n]`，返回`-1`。

完整代码如下，也可见[solve.py](./solve.py)。
```python
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        lines = []
        for i in range(len(ranges)):
            lines.append([i - ranges[i], i + ranges[i]])
        # 通过题目的输入，得到所有可选择的线段
        left, count = 0, 0
        while left < n: # 当left > n时，表明区间被完全覆盖
            right = 0
            for i, j in lines:
                if i <= left and j > right:
                    right = j
                # 找出左端点小于left的最长的线段，right记录其右端点
            if right > left: # 如果right > left说明找到了满足条件的线段，找不到则返回-1，说明这些线段无法覆盖区间
                count += 1
                left = right
            else:
                count = -1
                break
        return count
```

## 其他解法
还有动态规划也可以解这题，具体思路在[link](https://leetcode-cn.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/solution/guan-gai-hua-yuan-de-zui-shao-shui-long-tou-shu-3/)。