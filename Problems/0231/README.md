## 题目描述

给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。

**示例1：**

```
输入：n = 1
输出：true
解释：2^0 = 1
```

**示例2：**

```
输入：n = 16
输出：true
解释：2^4 = 16
```

**示例3：**

```
输入：n = 3
输出：false
```

**示例4：**

```
输入：n = 4
输出：false
```

**示例5：**

```
输入：n = 5
输出：false
```


## 题解思路

两个位运算方法：

* (n & (n - 1)) == 0
* (n & (-n)) == n

时间复杂度为 $O(1)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
};

```
