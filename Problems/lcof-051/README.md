## 题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

**示例：**
```
输入: [7,5,6,4]
输出: 5
```

## 题解思路
最容易想到的就是暴力枚举，但此题的例子中有的数组过长会发生TLE。其次便是归并排序，在归并排序的合并过程当中，会进行比较，在比较的同时进行计数。代码如下，也可见[solve.py](solve.py)。

```python
class Solution:
    def reversePairs1(self, nums: list[int]) -> int:
        temp = [0] * len(nums)
        def guibing(l, r):
            if l >= r: return 0
            mid = (l + r) // 2
            ans = guibing(l, mid) + guibing(mid + 1, r)
            temp[l:r + 1] = nums[l:r + 1]
            i, j = l, mid + 1
            for k in range(l, r + 1):
                # 例如[2, 3, 6, 7]和[0, 1, 4, 5]合并的时候第一个比较的便是2和0，这样就说明2以及2后面的数字都可以和0形成一个逆序对
                if i == mid + 1:
                    nums[k] = temp[j]
                    j += 1
                elif j == r + 1 or temp[i] <= temp[j]:
                    nums[k] = temp[i]
                    i += 1
                else:
                    nums[k] = temp[j]
                    j += 1
                    ans += mid - i + 1
            return ans

        return guibing(0, len(nums) - 1)
```

另一种解法就是树状数组。**树状数组**是一种可以动态维护序列前缀和的数据结构，它的功能是：
- **单点更新** update(i, v)： 把序列i位置的数加上一个值 vv，这题`v = 1`
- **区间查询** query(i)： 查询序列`[1, i]`区间的区间和，即i位置的前缀和

修改和查询的时间复杂度都是$O(logn)$，其中n为需要维护前缀和的序列的长度。

我们随意假设一个数组`a = [5, 5, 2, 3, 6]`，记录每个数字出现的次数，即为：
```
index  ->  1 2 3 4 5 6 7 8 9
value  ->  0 1 1 0 2 1 0 0 0
```
第`i - 1`个数的前缀和便是，有多少个数比`i`小。那当从后往前遍历序列`a`，记当前遍历到的元素为$a_i$，$a_i$出现的次数加一，并把`i - 1`位置的前缀和加入到答案中去，此时的前缀和便表示从后往前已经出现的比$a_i$小的数字的出现次数之和。代码如下，也可见[solve.py](solve.py)。

```python
class Solution:
    def reversePairs2(self, nums: list[int]) -> int:
        class FenwickTree:
            def __init__(self, n):
                self.size = n
                self.tree = [0 for _ in range(n + 1)]

            def __lowbit(self, index):
                return index & (-index)

            # 单点更新：将 index 这个位置 + 1
            def update(self, index, delta):
                # 从下到上，最多到 size，可以等于 size
                while index <= self.size:
                    self.tree[index] += delta
                    index += self.__lowbit(index)

            # 区间查询：查询小于等于 index 的元素个数
            # 查询的语义是"前缀和"
            def query(self, index):
                res = 0
                # 从上到下，最少到 1，可以等于 1
                while index > 0:
                    res += self.tree[index]
                    index -= self.__lowbit(index)
                return res
        size = len(nums)
        if size == 0 or size == 1: return 0
        # 去重
        s = list(set(nums))
        len_s = len(s)
        import heapq
        heapq.heapify(s)
        rank_map = dict()
        rank = 1
        for _ in range(len_s):
            num = heapq.heappop(s)
            rank_map[num] = rank
            rank += 1
        fenwick_tree = FenwickTree(len_s)
        res = 0
        # 从后向前填表
        for index in range(size - 1, -1, -1):
            # 1、查询排名
            rank = rank_map[nums[index]]
            # 2、在树状数组排名的那个位置 + 1
            fenwick_tree.update(rank, 1)
            # 3、查询一下小于等于“当前排名 - 1”的元素有多少
            res += fenwick_tree.query(rank - 1)
        return res
```