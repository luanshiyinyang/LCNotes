## 题目描述

为了不在赎金信中暴露字迹，从杂志上搜索各个需要的字母，组成单词来表达意思。

给你一个赎金信 (ransomNote) 字符串和一个杂志(magazine)字符串，判断 ransomNote 能不能由 magazines 里面的字符构成。

如果可以构成，返回 true ；否则返回 false 。

magazine 中的每个字符只能在 ransomNote 中使用一次。

**示例1：**

```
输入：ransomNote = "a", magazine = "b"
输出：false
```

**示例2：**

```
输入：ransomNote = "aa", magazine = "ab"
输出：false
```

**示例3：**

```
输入：ransomNote = "aa", magazine = "aab"
输出：true
```

## 题解思路

用哈希表保存 magazine 中元素出现的次数，再遍历 ransomNote ，若元素在哈希表中不存在，则返回 false ，都存在则返回 true 。

时间复杂度为 $O(m+n)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution
{
public:
    bool canConstruct(string ransomNote, string magazine)
    {
        unordered_map<char, int> myMap;
        for (auto c : magazine)
        {
            myMap[c]++;
        }
        for (auto c : ransomNote)
        {
            if (myMap[c] == 0)
            {
                return false;
            }
            myMap[c]--;
        }
        return true;
    }
};

```
