## 题目描述

给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。

换句话说，s1 的排列之一是 s2 的 **子串** 。

**示例1：**

```
输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
```

**示例2：**

```
输入：s1= "ab" s2 = "eidboaoo"
输出：false
```

## 题解思路

滑动窗口的思路，设 $m$ 、 $n$ 分别为 $s1$ 和 $s2$ 的长度。比较 $s2$ 中所有长度为 $m$ 的子序列，若存在子串等于 $s1$ 的排列之一，则返回 $true$ ，否则返回 $false$ 。

时间复杂度为 $O(m+n)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution
{
public:
    bool checkInclusion(string s1, string s2)
    {
        vector<int> ch1(26), ch2(26);
        int m = s1.size(), n = s2.size();
        if (m > n)
            return false;
        for (int i = 0; i < m; i++)
        {
            ch1[s1[i] - 'a']++;
            ch2[s2[i] - 'a']++;
        }
        if (ch1 == ch2)
        {
            return true;
        }
        for (int j = m; j < n; j++)
        {
            ch2[s2[j - m] - 'a']--;
            ch2[s2[j] - 'a']++;
            if (ch1 == ch2)
            {
                return true;
            }
        }
        return false;
    }
};

```
