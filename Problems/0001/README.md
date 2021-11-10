## 题目描述

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 **和为目标值 target**  的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

**示例1：**

```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
```

**示例2：**

```
输入：nums = [3,2,4], target = 6
输出：[1,2]
```

**示例3：**

```
输入：nums = [3,3], target = 6
输出：[0,1]
```

## 题解思路

用哈希表记录出现的数字和位置。遍历数组，若哈希表存在与当前数字和为 $target$ 的值，则输出结果，否则，将当前数字和位置加进哈希表。

时间复杂度为 $O(n)$ ，空间复杂度为 $O(n)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> myMap;
        vector<int> res;
        for (int i = 0; i < nums.size(); i++){
            unordered_map<int, int>::iterator it = myMap.find(target - nums[i]);
            if(it != myMap.end()){
                res.push_back(i);
                res.push_back(it->second);
                break;
            }
            myMap[nums[i]] = i;
        }
        return res;
    }
};

```
