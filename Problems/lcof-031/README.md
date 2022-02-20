## 题目描述

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

**示例1：**
```
输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
```
**示例2：**
```
输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。
```

## 题解思路

这道题其实我们笔试的时候很容易遇到的选择题，就是给定入栈序列，找出不可能的出栈序列。我们可以采用模拟的方法来实现一个栈，当遇到出栈元素的时候就出栈所有匹配的元素，如果最终栈内为空，那么代表该出栈序列合理。

代码实现如下，也可见于[solve.py](./solve.py)。

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return len(stack) == 0
```

上述解法的时间复杂度为$O(N)$，每个元素最多一次出入栈操作；空间复杂度为$O(N)$，需要一个辅助栈。