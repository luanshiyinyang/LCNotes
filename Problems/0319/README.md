## 题目描述

初始时有 `n` 个灯泡处于关闭状态。第一轮，你将会打开所有灯泡。接下来的第二轮，你将会每两个灯泡关闭一个。

第三轮，你每三个灯泡就切换一个灯泡的开关（即，打开变关闭，关闭变打开）。第 `i` 轮，你每 `i` 个灯泡就切换一个灯泡的开关。直到第 `n` 轮，你只需要切换最后一个灯泡的开关。

找出并返回 `n` 轮后有多少个亮着的灯泡。

**示例 1：**

![](https://i.loli.net/2021/11/16/PsFek4KNZjqm5ty.jpg)

```
输入：n = 3
输出：1 
解释：
初始时, 灯泡状态 [关闭, 关闭, 关闭].
第一轮后, 灯泡状态 [开启, 开启, 开启].
第二轮后, 灯泡状态 [开启, 关闭, 开启].
第三轮后, 灯泡状态 [开启, 关闭, 关闭]. 

你应该返回 1，因为只有一个灯泡还亮着。
```

**示例 2：**

```
输入：n = 0
输出：0
```

**示例 3：**

```
输入：n = 1
输出：1
```

## 题解思路

这道题其实可以整理一下题意：第$i$轮改变所有编号为$i$的倍数的灯泡的状态。一个编号为$x$的灯泡经过$n$轮后处于打开状态的充要条件为“该灯泡被切换状态次数为奇数次”。同时，一个灯泡切换状态的次数为其因数的个数（去重）。

于是问题转化为，在$[1,n]$内有多少个数，其因数的个数为奇数，这些位置的灯泡就是最后亮着的灯泡。

根据因数的概念，如果一个数$k$为$x$的因数，那么$\frac{x}{k}$必为$x$的因数，也就是因数一定成对出现。那么如果有一个数的因数为奇数个，显然有其中一个因数出现了两次且在同一次分解中出现（如$9=3 \times 3$），也就是$x$为完全平方数。

因此问题最终转化为，**在$[1,n]$中完全平方数的个数有多少个**。显然，我们知道，这个值就是$[1-n]$中最大的完全平方数开根的值，因此答案为$\lfloor \sqrt{x} \rfloor$。

上述解法的代码如下，也可见于[solve.py](./solve.py)。

```python
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
```