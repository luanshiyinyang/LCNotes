## 题目描述

给定一个整数数组，判断是否存在重复元素。

如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

**示例1：**

```
输入: [1,2,3,1]
输出: true
```

**示例2：**

```
输入: [1,2,3,4]
输出: false
```

**示例3：**

```
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
```

## 题解思路

用哈希表记录每个数字出现的次数，若有数字的次数大于1，则返回 true ，若所有数字的次数小于等于1，则返回 false。

时间复杂度为 $O(n)$ ，空间复杂度为 $O(n)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> myMap;
        for(int num : nums){
            if(myMap.find(num) != myMap.end()){
                return true;
            }
            myMap.insert(num);
        }
        return false;
    }
};

```
