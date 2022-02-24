## 题目描述
给定一个数组`A[0,1,…,n-1]`，请构建一个数组`B[0,1,…,n-1]`，其中`B[i]`的值是数组`A`中除了下标`i`以外的元素的积, 即`B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]`。不能使用除法。

**示例：**
```
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
```

## 题解思路
这题难就难在不能用除法，这里由于画图更加易懂，直接贴[K神的解析](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/solution/mian-shi-ti-66-gou-jian-cheng-ji-shu-zu-biao-ge-fe/)。其实也可以看做采用两次动态规划，分别计算出当前数字左边所有数的乘积和右边所有数的乘积，然后省去$O(n)$的空间，代码如下，也可见[solve.py](solve.py)。
```python
class Solution:
    def constructArr(self, a: list[int]) -> list[int]:
        b, temp = [1] * len(a), 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1] # 下三角乘积和，也就是当前数左边所有数的乘积和
        for i in range(len(a) - 2, -1, -1):
            temp *= a[i + 1] # 上三角乘积和，也就是当前数右边所有数的乘积和
            b[i] *= temp # 上三角乘下三角即所求
        return b
```