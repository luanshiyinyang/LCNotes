## 题目描述

给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

**示例：**

```
输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"
```

## 题解思路

双指针的思路，找到两指针的指向，并依次交换位置，即可解决问题。

时间复杂度为 $O(n)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution {
public:
    string reverseWords(string s) {
        int i = 0, left, right;
        while (i < s.size()) {
            left = i;
            while (s[i] != ' ' && i < s.size()) {
                i++;
            }
            right = i - 1;
            while (left < right){
                swap(s[left++], s[right--]);
            }
            i++;
        }
        return s;
    }
};

```
