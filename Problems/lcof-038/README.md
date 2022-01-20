## 题目描述
输入一个字符串，打印出该字符串中字符的所有排列。你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

**示例1**
```
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
```

## 题解思路
首先，按照最简单的思路，一个字符一个字符的插入，加入当前已有字符串为`['ab', 'ba']`，那么第三个字符进行插入，列表中每个字符串都能生成两个字符串，即`['cab', 'acb', 'abc', 'cba', 'bca', 'bac']`。以此类推，进行循环。

代码如下，也可见[solve.py](solve.py)。

```python
class Solution:
    def permutation1(self, s: str) -> list[str]:
        s = list(s)
        pool = collections.deque()
        pool.append(s[0])
        i = 1
        while i <= len(s) - 1:
            ins = s[i]
            while len(pool[0]) == i:
                temp = list(pool.popleft())
                for index in range(0, i + 1):
                    tempi = temp.copy()
                    tempi.insert(index, ins)
                    tempi = ''.join(tempi)
                    if tempi not in pool:
                        pool.append(tempi)
            i += 1
        return list(pool)
```

其次，正规一点的解法便是回溯。
递归解析：
1. 终止条件：当当前字符串长度`x == len(s) - 1`时，说明所有位置都已固定好，将当前结果保存，并返回；
2. 开始递归：初始化一个set，用于排除重复的字符；将当前索引为`x`的字符与索引（`i`）在`x`到`len(s) - 1`之间的字符一一进行交换；
3. 若`s[i]`在set中，代表它是重复的，进行“剪枝”；
4. 交换`s[i]`和`s[x]`，并将`s[i]`加入set中；
5. 开始下一层递归，调用dfs(x+1)，考虑第`x+1`个字符；
6. 再将`s[x]`和`s[i]`交换回来，“回溯”；

代码如下，也可见[solve.py](solve.py)。

```python
class Solution:
    def permutation2(self, s: str) -> list[str]:
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))   # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic: continue # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1)               # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i]  # 恢复交换
        dfs(0)
        return res
```