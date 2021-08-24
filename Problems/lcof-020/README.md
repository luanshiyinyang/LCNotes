## 题目描述

请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。

**数值**（按顺序）可以分成以下几个部分（翻译一下就是首尾若干个空格中间夹着一个小数或者整数）：

1. 若干空格
2. 一个 小数 或者 整数
3. （可选）一个 'e' 或 'E' ，后面跟着一个 整数
4. 若干空格

关于整数和小数的定义如下。

**小数**（按顺序）可以分成以下几个部分：

1. （可选）一个符号字符（'+' 或 '-'）
2. 下述格式之一：
   - 至少一位数字，后面跟着一个点 '.'
   - 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
   - 一个点 '.' ，后面跟着至少一位数字

**整数**（按顺序）可以分成以下几个部分：

1. （可选）一个符号字符（'+' 或 '-'）
2. 至少一位数字

部分数值列举如下：
```
["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]
```
部分非数值列举如下：
```
["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]
```


## 题解思路

这类按照给定条件判断字符串格式是否符合要求的题目在面试中还是比较常见的，常规的思路有**逻辑判断法**、**正则表达式**以及**该题特定解法**。

### 逻辑判断法

顾名思义，就是针对题目中给定的条件，组合出合适的判断语句来判断字符串是否合乎要求。而本题只需要一遍遍历所有字符并利用几个标志位防止重复即可实现题目的目的，**具体判断的逻辑如下面代码的注释所示**。

完整代码如下。

```python
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()  # 去除首尾空格
        dot, digit, e_E = False, False, False  # dot和e_E表示是否出现过小数点和e/E，而digit表示是否出现过数字并且最终决定该字符串是否合法

        for i, char in enumerate(s):
            if char in ('+', '-'):
                # 若为正负号，那么必为首个元素或者e/E后面的第一个元素，其余情况不合法
                if i > 0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
            elif char == '.':
                # 若为小数点，则不能已经出现过小数点或者出现在e/E后面，否则不合法
                if dot or e_E: 
                    return False
                dot = True
            elif char == 'e' or char == 'E':# 若为e/E，则不能已经出现过e/E，且前面必须出现了数字，否则均不合法
                if e_E or not digit:
                    return False
                e_E, digit = True, False # 这里e/E后面必须存在整数，因此它不能为最后一个元素，而digit同时作为最终返回值此处应当重置
            elif char.isdigit():
                digit = True
            else:
                return False
        return digit
```

### 正则表达式

毫不夸张的说，正则表达式几乎是字符串匹配的通用解法，但是前提是写得出合乎条件的正则表达式，按照上一节的解法，不难得到，本体的正则表达式为`^[+-]?(\.\d+|\d+\.?\d*)([eE][+-]?\d+)?$`。

完整代码如下，也可见[solve.py](./solve.py)。

```python
class Solution:
    def isNumber(self, s: str) -> bool:
        return re.compile('^[+-]?(\.\d+|\d+\.?\d*)([eE][+-]?\d+)?$').match(s.strip()) is not None
```

### 该题特定解法

本体可以按照确定性有限自动机模型来进行分析求解，这部分涉及到编译原理的一些只是，感兴趣的可以参考[官方题解](https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/biao-shi-shu-zhi-de-zi-fu-chuan-by-leetcode-soluti/)，解释得非常详细，我这里不多做赘述了，不过，该方法的效率不是很高。

代码如下。
```python
from enum import Enum

class Solution:
    def isNumber(self, s: str) -> bool:
        State = Enum("State", [
            "STATE_INITIAL",
            "STATE_INT_SIGN",
            "STATE_INTEGER",
            "STATE_POINT",
            "STATE_POINT_WITHOUT_INT",
            "STATE_FRACTION",
            "STATE_EXP",
            "STATE_EXP_SIGN",
            "STATE_EXP_NUMBER",
            "STATE_END"
        ])
        Chartype = Enum("Chartype", [
            "CHAR_NUMBER",
            "CHAR_EXP",
            "CHAR_POINT",
            "CHAR_SIGN",
            "CHAR_SPACE",
            "CHAR_ILLEGAL"
        ])

        def toChartype(ch: str) -> Chartype:
            if ch.isdigit():
                return Chartype.CHAR_NUMBER
            elif ch.lower() == "e":
                return Chartype.CHAR_EXP
            elif ch == ".":
                return Chartype.CHAR_POINT
            elif ch == "+" or ch == "-":
                return Chartype.CHAR_SIGN
            elif ch == " ":
                return Chartype.CHAR_SPACE
            else:
                return Chartype.CHAR_ILLEGAL
        
        transfer = {
            State.STATE_INITIAL: {
                Chartype.CHAR_SPACE: State.STATE_INITIAL,
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
                Chartype.CHAR_SIGN: State.STATE_INT_SIGN
            },
            State.STATE_INT_SIGN: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT
            },
            State.STATE_INTEGER: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_POINT: State.STATE_POINT,
                Chartype.CHAR_SPACE: State.STATE_END
            },
            State.STATE_POINT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_SPACE: State.STATE_END
            },
            State.STATE_POINT_WITHOUT_INT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION
            },
            State.STATE_FRACTION: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_SPACE: State.STATE_END
            },
            State.STATE_EXP: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                Chartype.CHAR_SIGN: State.STATE_EXP_SIGN
            },
            State.STATE_EXP_SIGN: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER
            },
            State.STATE_EXP_NUMBER: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                Chartype.CHAR_SPACE: State.STATE_END
            },
            State.STATE_END: {
                Chartype.CHAR_SPACE: State.STATE_END
            },
        }

        st = State.STATE_INITIAL
        for ch in s:
            typ = toChartype(ch)
            if typ not in transfer[st]:
                return False
            st = transfer[st][typ]
        
        return st in [State.STATE_INTEGER, State.STATE_POINT, State.STATE_FRACTION, State.STATE_EXP_NUMBER, State.STATE_END]
```

### 试错法

最后再补充一个不太常规甚至有点取巧的方法，那就是，其实本体的合法数值都是可以自动转换为Python的浮点小数的（**在Python中，科学计数表示的数是float型**），因此只需要尝试一下是否可以转换即可。

代码如下。
```python
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except :
            return False
```




