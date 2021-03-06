## 题目描述

编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。

**提示：**
- 请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
- 在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在下面的 示例 3 中，输入表示有符号整数 -3。

**示例1：**
```
输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
```

**示例2：**
```
输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
```

**示例3：**
```
输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
```

**补充说明：**
- 输入必须是长度位32的二进制串。

## 题解思路

这题最直观的思路，就是32位二进制，干脆就逐个位置判断是不是1（第n位是1的话，那么这个数与$2^n$的"与运算"的结果为1）。

代码如下。

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if (n & 1 << i):
                count += 1
        return count
```

可以发现，这个解法的时间复杂度是$O(k)$，k为数字的二进制位数；空间复杂度显然为$O(1)$。

## 优化思路

优化的思路来源于一个运算性质：n & (n-1)的运算结果其实是将n这个数字的二进制串中的最后一个1变为0的结果。举个例子，$6=(110)_2$，$5=(101)_2$，$4=(100)_2$，有`6 & (6-1) = 4`，其实就是将6的二进制串`110`中的最后一个1（正数第二位）变为了0。

有了这个性质，只需要多次执行n和n-1的与运算，看需要多少次运算n变为0，这个运算次数就是原数字含有的1的个数。

代码如下，也可见于[solve.py](./solve.py)。

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n-1)
            count += 1
        return count
```

上述解法的时间复杂度为$O(logn)$，最坏情况下n的所有位数均为1，需要循环$logn$次。空间复杂度为$O(n)$。