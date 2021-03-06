## 题目描述

给定一个**偶数**长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果**平均**分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。

**示例1：**

```
输入: candies = [1,1,2,2,3,3]
输出: 3
解析: 一共有三种种类的糖果，每一种都有两个。
     最优分配方案：妹妹获得[1,2,3],弟弟也获得[1,2,3]。这样使妹妹获得糖果的种类数最多。
```

**示例2：**

```
输入: candies = [1,1,2,3]
输出: 2
解析: 妹妹获得糖果[2,3],弟弟获得糖果[1,1]，妹妹有两种不同的糖果，弟弟只有一种。这样使得妹妹可以获得的糖果种类数最多。
```

## 题解思路

当所有糖果种类数大于总糖果数量的一半时，妹妹可以获得的糖果种类数为总糖果的一半，当所有糖果种类数小于总糖果数量的一半时时，妹妹可以获得的糖果种类数为所有糖果种类数。

时间复杂度为 $O(n)$ ，空间复杂度为 $O(n)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        unordered_set<int> mySet(candyType.begin(), candyType.end());
        return min(candyType.size() / 2, mySet.size());
    }
};

```
