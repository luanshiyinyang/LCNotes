## 题目描述

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

* 左括号必须用相同类型的右括号闭合。
* 左括号必须以正确的顺序闭合。

**示例1：**

```
输入：s = "()"
输出：true
```

**示例2：**

```
输入：s = "()[]{}"
输出：true
```

**示例3：**

```
输入：s = "(]"
输出：false
```

**示例4：**

```
输入：s = "([)]"
输出：false
```

**示例5：**

```
输入：s = "{[]}"
输出：true
```

## 题解思路

用栈保存所有左括号，若栈顶左括号匹配到相应的右括号，则出栈，否则返回 false 。

时间复杂度为 $O(n)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution
{
public:
    bool isValid(string s)
    {
        stack<char> stk;
        unordered_map<char, char> myMap = {{')', '('}, {']', '['}, {'}', '{'}};
        for (auto x : s)
        {
            if (myMap.find(x) == myMap.end())
            {
                stk.push(x);
            }
            else if (stk.size() != 0 && myMap[x] == stk.top())
            {
                stk.pop();
            }
            else
            {
                return false;
            }
        }
        return stk.empty();
    }
};

```
