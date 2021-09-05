## 题目描述

给定一个只包含a和c的字符串，通过交换相邻两个字符的方式消除掉字符串中的"ac"，求解至少要进行多少次交换操作。

```
s = "acca"
输出应为2
```

## 题解思路

本题乍看是个编辑距离的题目，但是其实没有那么复杂，目标字符串其实就是所有的c在a前面这个结果，那么只需要计算原始字符串到目标字符串通过"相邻交换"这个操作需要多少步到达即可，可以采用双指针来实现。



下面是完整的代码，也可见于[solve.py](./solve.py)。
```python
class Solution(object):
    def solve(self, s: str):
        flag, num = 0, 0
        for i in range(len(s)):
            if s[i] == 'c':
                num += (i - flag)
                flag += 1
        return num
```

