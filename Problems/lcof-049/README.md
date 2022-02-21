## 题目描述
我们把只包含质因子`2`、`3`和`5`的数称作丑数（Ugly Number）。求按从小到大的顺序的第`n`个丑数。

**示例：**
```
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
```

## 题解思路
首先最简答的便是枚举，判断每一个数除以2、3和5后是不是结果为1，但这样会TLE。

其次想到的便是，若`x`是丑数，那么`2x`，`3x`，`5x`也是丑数，那我们维护一个最小堆，其初始化为`[1]`，每次将其中的堆顶元素`x`弹出，计算其`2x`，`3x`，`5x`，若这些数未出现过（通过维护一个seen字典或列表来判断），则将其push到最小堆中，这样以来，第`n`次从堆顶弹出的元素便是所求，代码如下，也可见[solve.py](solve.py)。
```python
class Solution:
    def nthUglyNumber1(self, n: int) -> int:
        # 最小堆
        ugly = [2, 3, 5]
        heap = [1]
        uglys = [1]
        for _ in range(n - 1):
            small = heapq.heappop(heap)
            for u in ugly:
                if small * u not in uglys:
                    heapq.heappush(heap, small * u)
                    uglys.append(small * u)
        return heapq.heappop(heap)
```

其次，这种形式的题目很显然是可以递推的，所以还可以用动态规划进行求解。跟前一个解法的思路类似，所有的丑数都是从更小的丑数“×2”、“×3”或“×5”得到的，最小的丑数为“1”，所有的丑数都可以从1得到。我们维护三个指针，表示下一个丑数是当前指针指向的丑数乘以对应的质因数，`p2`, `p3`, `p5`。我们将各个指针所指的数乘以对应的“2，3或5”后，其中最小的一个便是下一个丑数，那将那个指针往后移动。代码如下，也可见[solve.py](solve.py)。
```python
class Solution:
    def nthUglyNumber2(self, n: int) -> int:
        ans = [0] * (n + 1)
        p2, p3, p5 = 1, 1, 1
        ans[1] = 1
        for i in range(2, n + 1):
            num2, num3, num5 = ans[p2] * 2, ans[p3] * 3, ans[p5] * 5
            num = min(num2, num3, num5)
            ans[i] = num
            if num == num2:
                p2 += 1
            if num == num3:
                p3 += 1
            if num == num5:
                p5 += 1
        # print(ans)
        return ans[n]
```

**PS：** 需要注意的是，最后的三个判断为：

```python
if num == num2:
    p2 += 1
if num == num3:
    p3 += 1
if num == num5:
    p5 += 1
```
不能写成以下形式：
```python
if num == num2:
    p2 += 1
elif num == num3:
    p3 += 1
elif num == num5:
    p5 += 1
```
这是为了防止重复的数出现的情况，比如当`p2`指向2，`p3`指向2，`p5`指向2时，最小的下一个丑数为6，而2×3和3×2都为6，所以指针`p2`和`p3`均要向后移动，不然会出现两个6。