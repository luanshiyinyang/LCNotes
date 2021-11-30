# 题目描述
给你一个按递增顺序排序的数组 arr 和一个整数 k 。数组 arr 由 1 和若干 素数  组成，且其中所有整数互不相同。
对于每对满足 $0 < i < j < arr.length$ 的 $i$ 和 $j$ ，可以得到分数 $arr[i] / arr[j]$ 。
那么第 $k$ 个最小的分数是多少呢?  以长度为 2 的整数数组返回你的答案, 这里 $answer[0] == arr[i]$ 且 $answer[1] == arr[j]$ 。

**示例1：**
```
输入：arr = [1,2,3,5],  k = 3
输出：[2,5]
解释：已构造好的分数,排序后如下所示: 
1/5, 1/3, 2/5, 1/2, 3/5, 2/3
很明显第三个最小的分数是 2/5。
```

**示例2：**
```
输入：arr = [1,7], k = 1
输出：[1,7]
```

# 题解思路
记数组$arr$的长度为$n$。最简单粗暴的想法就是将所有的可能枚举出来，共$\frac{n(n - 1)}{2}$种可能，并将其排序，然后寻找第$k$个小的。这种解法虽然能过，但效率还是特别低的，时间复杂度为$O(n^{2}logn)$，空间复杂度为$O(n^{2})$。这问题大嘛？问题不大，能写出来就行，但咱就是说有没有看上去高级一点的方法，还是有的。
## 优先队列（堆）
其实得益于数组$arr$是递增的，所以在所有形成的分数中，是有顺序的。我们将分母记为$arr[j]$，对于每一个分母，记其分子为$arr[i]$。我们将每一个分母看成一个长度为$j$的列表，即：
$$
\frac{\operatorname{arr}[0]}{\operatorname{arr}[j]}, \frac{\operatorname{arr}[1]}{\operatorname{arr}[j]}, \cdots, \frac{\operatorname{arr}[j-1]}{\operatorname{arr}[j]}
$$
显而易见，这些列表是递增的。此时，我们要找到这$n-1$个列表中第$k$个最小的分数，可以采用优先队列来解决。初始时，优先队列里包含着$n-1$个分数（$\frac{\operatorname{arr}[0]}{\operatorname{arr}[1]}, \cdots, \frac{\operatorname{arr}[0]}{\operatorname{arr}[n-1]}$），每次从队列中选取最小的分数，$\frac{\operatorname{arr}[i]}{\operatorname{arr}[j]}$，如果$i+1=j$，说明这个分数是$\operatorname{arr}[j]$队列中最大的一个；如果$i+1<j$，说明我们选取了$\frac{\operatorname{arr}[i]}{\operatorname{arr}[j]}$只好要将$\frac{\operatorname{arr}[i+1]}{\operatorname{arr}[j]}$再放入队列中。此时的时间复杂度为$O(klogn)$，单次优先队列操作的复杂度为$O(logn)$，一共要执行$k$次，空间复杂度为$O(n)$。
代码如下，也可见[solve.py](./solve.py)：
```python
class Frac:
    def __init__(self, idx: int, idy: int, x: int, y: int) -> None:
        self.idx = idx
        self.idy = idy
        self.x = x
        self.y = y

    def __lt__(self, other: "Frac") -> bool:
    # python中的富比较方法，用于类之间的比较，比如对类的不同实例进行sort。
        return self.x * other.y < self.y * other.x


class Solution:
    def kthSmallestPrimeFraction1(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        q = [Frac(0, i, arr[0], arr[i]) for i in range(1, n)]
        # heapq是python中的用于实现堆的一个模块heapqify是将列表具有堆特征。
        heapq.heapify(q)
		
        for _ in range(k - 1):
            frac = heapq.heappop(q)
            i, j = frac.idx, frac.idy
            if i + 1 < j:
            	# 将arr[i + 1] / arr[j]放入优先队列中
                heapq.heappush(q, Frac(i + 1, j, arr[i + 1], arr[j]))
        
        return [q[0].x, q[0].y]
```

## 二分查找$+$双指针
如果我们能找到一个数$\alpha$，恰好有$k$个素数分数小于$\alpha$，那么这些分数中最大的就是我们要找的答案。首先，对于一个$\alpha$，我们如何找到有多少个比它小的素数分数呢？这时我们可以采用双指针。
- 设定指针$j$来指定分母，从左往右，每次枚举一个分母；
- 设定指针$i$来指定分子，从左往右移动，最小是$0$，最大是$j-1$，并且移动的过程中，还要保证$\frac{\operatorname{arr}[i]}{\operatorname{arr}[j]}<\alpha$成立。当$i$移动停止后，说明$\operatorname{arr}[0], \cdots, \operatorname{arr}[i]$都可以作为分子，即分母为$\operatorname{arr}[j]$的小于$\alpha$的素数分数一共有$i+1$个；
- 在$j$向右移动的过程中，将每个$j$对应的$i+1$累加起来，就是最终的小于$\alpha$的素数分数的个数；
- 在移动的时候，记录一个当前最大素数分数[x, y]；

那么如何找到我们需要的$\alpha$呢？如果上述过程最后的个数等于$k$，那说明选的$\alpha$刚刚好。如果个数小于$k$，那说明当前选取的$\alpha$过小；如果个数大于$k$，那说明当前选取的$\alpha$过大。这很明显，可以用二分查找来寻找最合适的$\alpha$。
代码如下，也可见[solve.py](./solve.py)：
```python
class Solution:
    def kthSmallestPrimeFraction2(self, arr: List[int], k: int) -> List[int]:
    	n = len(arr)
        left, right = 0.0, 1.0
        while True:
            mid = (left + right) / 2
            i, count = -1, 0
            x, y = 0, 1
            for j in range(1, n):
                while arr[i + 1] / arr[j] < mid:
                    i += 1
                    if arr[i] * y > x * arr[j]:
                        x, y = arr[i], arr[j]
                count += i + 1
            if count == k: return [x, y]
            if count < k:
                left = mid
            if count > k:
                right = mid
```
最终的时间复杂度为$O(nlogC)$，$C$为数组$arr$中的元素的上界，二分查找需要$\left\lceil\log C^{2}\right\rceil=O(\log C)$次。每一步需要$O(n)$的时间得到小于$\alpha$的素数分数的个数。空间复杂度为$O(1)$。