## 题目描述
给定一个`m x n`二维字符网格`board`和一个字符串单词`word`。如果`word`存在于网格中，返回`true`；否则，返回`false`。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

例如，在下面的`3×4`的矩阵中包含单词`"ABCCED"`（单词中的字母已标出）。

![](https://i.loli.net/2021/08/29/LaGENSbQ48Pomz1.png)

## 解题思路
这题还是很容易想到采用回溯法。先遍历所有节点找开头，然后对所有开头回溯，每轮回溯时分别往四个方向查看是否为下一个所需元素，若数组越界，或者与`word`中下一个字母不相等，则返回`false`。当回溯到最后一个元素，表示成功找到。思路其实比较简单，我觉得主要就是代码方面比较难搞懂。

## 复杂度分析
时间复杂度分析：

首先是方案数的计算，设字符长度为`K`，搜索时每个字符有上下左右四个方向，去掉上一个字符，那就是三种选择，因此搜索出正确的字符串的复杂度为`O(3^K)`。最差情况，遍历了矩形内`M*N`个字符，最终的时间复杂度为`O(3^(K)MN)`。

空间复杂度分析：

因为是递归实现，所以空间复杂度即为`O(K)`。当`K`最长等于`MN`时，空间复杂度为`O(MN)`。

## 代码分析
完整代码如下，也可见[solve.py](./solve.py)。

总的来说，回溯法的流程便是“破坏现场——dfs——还原现场”。
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            # 用来判断程序是否越界，还有第一个字母是否匹配，第一个都不匹配直接返回False
            if k == len(word) - 1: return True
            board[i][j] = ''
            # 把访问过的字母标记为空，这样可以避免程序多次访问同一元素
            ans = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            # 按照四个方向进行更深一层的寻找
            board[i][j] = word[k]
            # 一趟dfs结束后把原来设的空改回来，以免影响后面的dfs遍历使用
            return ans
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
         # 一个一个字母来尝试，每一次尝试都是dfs遍历成功的一种可能性，若是这个循环中都没找到True，则最终返回False
        return False
```