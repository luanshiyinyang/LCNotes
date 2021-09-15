## 题目描述
给你一个以字符串表示的非负整数`num`和一个整数`k`，移除这个数中的`k`位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。

**示例 1：**
```
输入：num = "1432219", k = 3
输出："1219"
解释：移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219 。
```

**示例 2：**
```
输入：num = "10200", k = 1
输出："200"
解释：移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
```

**示例3：**
```
输入：num = "10", k = 2
输出："0"
解释：从原数字移除所有的数字，剩余为空就是 0 。
```

## 题解思路
这题稍微简单的想法就是，移除掉`k`个数字，就相当于从非负整数`num`中挑选`len(num) - k`个数字形成最小的数字序列。采用单调栈的结构便可以，代码跟`leetcode-0321`题中的找到最大子序列的一样的思路，只不过这里是最小子序列。另外，这里如果前几个数字为`0`，比如`0200`，则需要将前面的`0`删掉，最后输出`200`。时间复杂度为`O(n)`，就算其中有嵌套的循环，次数也不会大于`n`；空间复杂度为`O(k)`或`O(n)`。

代码如下，也可见[solve.py](solve.py)
```python
def removeKdigits1(self, num: str, k: int) -> str:
        if k == len(num): return '0'
        res = len(num) - k
        stack = []
        for i in range(len(num)):
            if not stack: 
                stack.append(num[i])
            else:
                if stack[-1] <= num[i] and len(stack) < res:
                    stack.append(num[i])
                if stack[-1] > num[i]:
                    while stack[-1] > num[i] and len(num) - i > res - len(stack):
                        stack.pop()
                        if not stack: break
                    stack.append(num[i])

        for i in range(len(stack)):
            if stack[i] != '0':
                temp = i
                break
        stack = stack[i:]
        return ''.join(stack[i] for i in range(len(stack)))
```

另一条思路便是对单调栈栈顶元素弹出的次数进行统计，若最后删除的次数`m`小于`k`，则在序列最后再删除掉`m-k`个数字。

代码如下，也可见[solve.py](solve.py)。
```python
def removeKdigits2(self, num: str, k: int) -> str:
        numStack = []
        
        # 构建单调递增的数字串
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
        
            numStack.append(digit)
        
        # 如果 K > 0，删除末尾的 K 个字符
        finalStack = numStack[:-k] if k else numStack
        
        # 抹去前导零
        return "".join(finalStack).lstrip('0') or "0"
```