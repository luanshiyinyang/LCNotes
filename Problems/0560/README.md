## 题目描述

给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。

**示例1：**

```
输入：nums = [1,1,1], k = 2
输出：2
```

**示例2：**

```
输入：nums = [1,2,3], k = 3
输出：2
```

## 题解思路

前缀和的作用在于：将几个数字的和转化为两个数字的差，从而减少数字的比较。本题运用了前缀和的思路，并借助哈希表来存储相同的差。

时间复杂度为 $O(n)$ ，空间复杂度为 $O(n)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```cpp
class Solution
{
public:
    int subarraySum(vector<int> &nums, int k)
    {
        int res = 0;
        vector<int> sum;
        unordered_map<int, int> myMap;
        sum.push_back(0);
        for (int x : nums)
        {
            sum.push_back(sum.back() + x);
        }
        for (int i = sum.size() - 1; i >= 0; i--)
        {
            if (myMap.find(sum[i]) != myMap.end())
                res += myMap[sum[i]];
            else
                myMap[sum[i] - k]++;
        }
        return res;
    }
};

```
