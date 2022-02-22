## 题目描述
给定一个数组`nums`和滑动窗口的大小`k`，请找出所有滑动窗口里的最大值。

**示例：**
```
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

## 题解思路
首先最简单的想法就是暴力枚举，这样有TLE的风险。我们选择的方法是单调队列。但当入队列的时候，我们要保持其单调性，比如当前队列为`[5，3，2，1]`，当`4`进行入队操作时，它会将队列中的`3，2，1`给“挤出来”，队列更新为`[5，4]`。这是因为当某一时刻的滑动窗口的最大值为索引`i`，那么向下滑动一次后，若索引`i`依旧在窗口内，那么这次窗口的最大值也不可能在`i`的左边，所以在某一个数入队列时，可以把前面比自己小的给“挤出来”。这样队列的队首便是当前的最大值，但要注意的是队首不一定还在窗口内，所以要对索引进行判断。代码如下，也可见[solve.py](solve.py)。
```python
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if not nums: return []
        n, q = len(nums), collections.deque()
        for i in range(k): # 先把第一个窗口放入队列
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]: # 第i个数入队列
                q.pop()
            q.append(i)
            while q[0] <= i - k: # 判断队首是否在窗口内，如不在则直接弹出
                q.popleft()
            ans.append(nums[q[0]])
        return ans
```