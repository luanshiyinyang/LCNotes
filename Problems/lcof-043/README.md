## 题目描述
输入一个整数`n`，求`1～n`这`n`个整数的十进制表示中`1`出现的次数。

例如，输入`12`，`1～12`这些整数中包含`1`的数字有`1`、`10`、`11`和`12`，`1`一共出现了`5`次。

**示例1**
```
输入：n = 12
输出：5
```

**示例2**
```
输入：n = 13
输出：6
```

## 题解思路
这里采用的方法是考虑每一位上`1`出现的次数。我们以计算`n=1234567`的百位上的`1`出现的次数为例。首先，对于从`0`开始每`1000`个数，其百位上的数字`1`都会出现`100`次。比如[0, 999]，其中百位上出现了[100, 199]这一百个数字。[1000, 1999]中，百位上是`1`的数字有[1100, 1199]这一百个。而`n`有着`1234`个这样的循环，所以百位上出现了`1234*100`个`1`。用`n`来表示就是：
$$
\left\lfloor\frac{n}{1000}\right\rfloor \times 100
$$
假设`r = n mod 1000 = 567`，那么我们还需要计算出在[0, r]中百位上出现`1`的次数，很明显这需要分情况讨论：

- 当`r`小于`100`时，百位上没有1；
- 当`r`在`[100, 200)`区间时，出现的次数为`r - 100 + 1`;
- 当`r`大于200时，出现了100次；

可以写成`min(max(r - 100 + 1, 0), 100)`的形式。那么，总的次数便为：
$$
\left\lfloor\frac{n}{1000}\right\rfloor \times 100 + min(max(n \ mod \ 1000 - 100 + 1, 0), 100)
$$
用$10^k$来代表某一个数位：
$$
\left\lfloor\frac{n}{10^{k+1}}\right\rfloor \times 10^{k}+ min \left(max \left(n \bmod 10^{k+1}-10^{k}+1,0\right), 10^{k}\right)
$$

代码如下，也可见[solve.py](solve.py)。

```python
class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        mulk = 1
        while n >= mulk:
            count += (n // (mulk * 10)) * mulk + min(max(n % (mulk * 10) - mulk +1, 0), mulk)
            mulk *= 10
        return count
```