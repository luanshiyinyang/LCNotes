## 题目描述

给定两个数组，编写一个函数来计算它们的交集。

**示例1：**

```
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
```

**示例2：**

```
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
```

## 题解思路

有关重复的问题，首先想到哈希表。可用哈希表记录一个数组中所有出现数字及其次数，再遍历另一个数组，查找哈希表是否存在该数字，并更新输出。

时间复杂度为 $O(n)$ ，空间复杂度为 $O(n)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> myMap;
        vector<int> res;
        for (int num1 : nums1) {
            auto it = myMap.find(num1);
            if (it != myMap.end()) {
                it->second++;
            } else {
                myMap[num1] = 1;
            }
        }
        for (int num2 : nums2) {
            auto it = myMap.find(num2);
            if (it != myMap.end() && it->second > 0) {
                res.push_back(num2);
                it->second--;
            }
        }
        return res;
    }
};

```
