## 题目描述

给定一个字符串 s ，请你找出其中不含有重复字符的 **最长子串** 的长度。

**示例1：**

```
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

**示例2：**

```
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

**示例3：**

```
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

**示例4：**

```
输入: s = ""
输出: 0
```

## 题解思路

滑动窗口的思路，用字符串 $t$ 表示无重复字符的子串，依次向 $t$ 插入 $s$ 中的元素，若 $t$ 中含有该元素，则删除第一个元素，直至不含该元素为止，记录每次 $t$ 的长度，并返回最大值。

时间复杂度为 $O(n)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0, right = 0, res = 0;
        string t("");
        while (right < s.size()){
            while (t.find(s[right]) != string::npos) {
                t.erase(0, 1);
                left--;
            }
            t.insert(t.end(), s[right]);
            right++;
            res = max(res, right - left);
        }
        return res;
    }
};

```
