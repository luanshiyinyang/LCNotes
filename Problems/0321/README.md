## 题目描述
给定长度分别为`m`和`n`的两个数组，其元素由`0-9`构成，表示两个自然数各位上的数字。现在从这两个数组中选出`k(k <= m + n)`个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

求满足该条件的最大数。结果返回一个表示该最大数的长度为`k`的数组。

**示例 1：**
```
输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]
```

**示例 2：**
```
输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
```

**示例 3：**
```
输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]
```

## 题解思路
假设最后的答案由数组`nums1`中的子序列`x`和数组`nums2`中的子序列`y`组成，这题最主要的一点就是要想到最终的答案是最大的，所以`x`和`y`也是各自数组同等长度的子序列中数值最大的。所以这题的思路便不难想到：首先得到所有可能的`k1+k2=k`，且`k1`和`k2`小于`nums1`和`nums2`的长度，然后找到`nums1`中长度为`k1`的最大子序列`x`，以及`nums2`中长度为`k2`的最大子序列`y`，再找到`x`和`y`拼接出来的数值最大的组合，即为答案。步骤较多，所以代码比较多。

代码如下，也可见[solve.py](solve.py)。

首先是找到固定长度的最大子序列的函数：
```python
def find_max_subseqence(n:List[int], k:int):
            if k == 0: return []
            stack = []
            for i in range(len(n)):
                if not stack:
                    stack.append(n[i])
                else:
                    if stack[-1] >= n[i] and len(stack) < k:
                        stack.append(n[i])
                    if stack[-1] < n[i]:
                        while stack[-1] < n[i] and len(n) - i > k - len(stack):
                            stack.pop()
                            if not stack:
                                break
                        stack.append(n[i])
            return stack
```
然后是将两个子序列融合的函数：
```python
def merge(subsequence1: List[int], subsequence2: List[int]) -> List[int]:
            x, y = len(subsequence1), len(subsequence2)
            if x == 0:
                return subsequence2
            if y == 0:
                return subsequence1
        
            mergeLength = x + y
            merged = list()
            index1 = index2 = 0

            for _ in range(mergeLength):
                if compare(subsequence1, index1, subsequence2, index2) > 0:
                    merged.append(subsequence1[index1])
                    index1 += 1
                else:
                    merged.append(subsequence2[index2])
                    index2 += 1
        
            return merged
```
以及两个数组比较大小的函数：
```python
def merge(subsequence1: List[int], subsequence2: List[int]) -> List[int]:
            x, y = len(subsequence1), len(subsequence2)
            if x == 0:
                return subsequence2
            if y == 0:
                return subsequence1
        
            mergeLength = x + y
            merged = list()
            index1 = index2 = 0

            for _ in range(mergeLength):
                if compare(subsequence1, index1, subsequence2, index2) > 0:
                    merged.append(subsequence1[index1])
                    index1 += 1
                else:
                    merged.append(subsequence2[index2])
                    index2 += 1
        
            return merged
```
这里需要注意的是，`compare`函数在进行比大小的时候，当当前位置的数字相等时，需要继续往后看，继续比大小，而且在`merge`时，不能因为两个数字相等便随意填一个，例如`6，7`和`6，0，4`，如果因为第一个位置的`6`相等，就选了后面的一个序列的`6`，那么形成的数列是`66704`，而如果选取第一个`6`，则是`67604`，所以需要这种两个数字一样大的时候，需要继续往后判断，往后便是`7>0`，所以选取第一个`6`，最终答案是`67604`。