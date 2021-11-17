## 题目描述

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

**注意**：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

**示例1：**

```
输入: s = "anagram", t = "nagaram"
输出: true
```

**示例2：**

```
输入: s = "rat", t = "car"
输出: false
```

## 题解思路

用哈希表保存 s 和 t 中元素出现的次数，若哈希表相等，则返回 true，否则返回 false。

时间复杂度为 $O(m+n)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        unordered_map<char, int> myMap;
        for (auto c : s)
        {
            myMap[c]++;
        }
        for (auto c : t)
        {
            myMap[c]--;
        }
        for (auto x : myMap)
        {
            if (x.second != 0)
            {
                return false;
            }
        }
        return true;
    }
};

```
