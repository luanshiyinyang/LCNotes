## 题目描述

以数组 `intervals` 表示若干个区间的集合，其中单个区间为 `intervals[i] = [starti, endi]` 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

**示例1**
```
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
```
**示例2**
```
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
```

## 题解思路

本题是线段重叠问题的典型问题之一，即合并重叠线段。可以证明，其实如果按照每个线段的左端点进行升序排序，那么可以合并的线段在排序后的列表中一定是连续的，如下图所示，其中蓝色、黄色和绿色三个区域可以合并为一个大区间。

![](https://i.loli.net/2021/09/01/6KtQE9GWqglzv1H.png)

实现上，我们可以一遍遍历排序后的整个线段列表，并比较当前线段与合并后的线段列表`merged`的最后一个元素之间的关系。若`merged`的最后线段的右端点还在当前线段的左端点左侧，那么他们是无法合并的，这个线段直接作为合并后的线段列表`merged`的最后一项即可；若上述判断失败，则表示`merged`的最后一项与当前线段有重合，将当前线段更新到`merged`的最后一项中（具体操作为将`merged`的最后一项的右端点更新为原来的值和当前线段右端点的值的较大者）。


完整代码如下，也可见[solve.py](./solve.py)。

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 升序排序线段列表
        intervals.sort(key=lambda x: x[0])
        # 创建合并后的结果
        merged = []
        for interval in intervals:
            # 无需合并
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # 需要合并
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
```

