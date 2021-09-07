## 题目描述

假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。


**示例 1：**
```
输入：flowerbed = [1,0,0,0,1], n = 1
输出：true
```
**示例 2：**
```
输入：flowerbed = [1,0,0,0,1], n = 2
输出：false
```

## 题解思路

本题非常典型且难度不大，面试中会有以此题为模板的题目。这题有采用数学推导的，但是大多数人还是采用贪心解法，**本题的官方题解略有点过于复杂了。**

其实思路非常简单，**即从左向右遍历数组，在可以放置1的情况就放1（能种就种，这是因为在任意能种的时候，不种都不会得到更优的解法），这是一种贪心的思想。**

那么对于任一位置，如何判断该位置能否填1（种花）呢？其实只要满足下面的三个条件即可。
- **自己为空（为0）**
- **左边为空（为0）** 或者 **自己是最左边**
- **右边为空（为0）** 或者 **自己是最右边**

我们只需要找出所有的可种位置数目，然后判断其是否大于需要中的数目即可。

因此我们可以得到如下的代码，也可见于[solve.py](./solve.py)。

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                count += 1
                flowerbed[i] = 1
        return count >= n
```

显然这段代码的时间复杂度为$O(n)$，空间复杂度为$O(1)$。**上述代码会存在一个隐患，那就是Python的List是可以越界的，也就是说对于一个arr而言，arr[len(arr)]和arr[-1]都是存在的，但是实际上这个问题不需要考虑因为我们的判断式中or的两个条件是精心设计的，前一个判断不通过才会进入后一个判断。**

## 优化思路

优化的思路其实也非常的简单，我们没必要算到最后才输出结果，若当前位置之前已经能种大于n个花了，那么直接返回True即可。

优化后的代码如下。

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                n -= 1
                if n <= 0:
                    return True
                flowerbed[i] = 1
        return n <= 0
```