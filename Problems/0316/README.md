## 题目描述
给你一个字符串`s`，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

**示例 1：**
```
输入：s = "bcabc"
输出："abc"
```

**示例 1：**
```
输入：s = "cbacdcbc"
输出："acdb"
```

## 题解思路
如果只是单纯地去除掉重复的字母，不打乱顺序，其实还是很简单的，但是这题还需要输出字典序最小的字符串。比较字典序需要从第一个字母开始，如果第一个相同，则比较第二个字符串，例如`abc < ac`、`abc < abd`。

我们采用一个单调栈来维护已经遍历的保存下来的字母。从左到右遍历字符串，对于每一个字符判断是否需要丢弃，如果已在栈中，则丢弃；如果该字符比栈顶的字母字典序小，且栈顶元素在剩下的字符串中依旧有，则将栈顶元素弹出，将此时遍历的字母放入栈中。

完整代码如下，也可见[solve.py](./solve.py)。

```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if not stack: # 如果栈空，直接进栈
                stack.append(s[i])
            else:
                if s[i] not in stack: # 判断当前遍历到的字母是否已在栈中
                    while stack[-1] > s[i] and stack[-1] in s[i:]: # 当栈顶元素字典序大于遍历的字母，且栈顶元素在之后的字符串也出现了，便可以弹出
                        stack.pop()
                        if not stack:
                            break
                    stack.append(s[i])
        return ''.join(stack[i] for i in range(len(stack)))
```