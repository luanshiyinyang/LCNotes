## 题目描述
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

**示例1：**
```
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
```

**示例2：**
```
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```

## 题解思路
一开始想到的依旧是暴力求解，编码简单，但时间有点长。然后就会思考，能不能在遍历一遍的情况下，解决问题。首先，用一个变量记住当前的最大利润，这是肯定的。除此之外，我们在遍历的时候，可以再用一个变量，记住到当前天为止，出现的历史最低价格，这样用每天的价格去与历史最低价格相比，要是利润更高，就更新最大利润，要是当天价格更低，就更新历史最低价格。代码如下，也可见[solve.py](solve.py)。

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices: return 0
        ans, mmin = 0, prices[0]
        for i in range(1, len(prices)):
            temp = prices[i] - mmin
            if temp > ans:
                ans = temp
            if prices[i] < mmin:
                mmin = prices[i]
        return ans
```