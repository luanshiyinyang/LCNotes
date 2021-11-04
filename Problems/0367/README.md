## 题目描述

给定一个 **正整数** num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

**进阶**：**不要** 使用任何内置的库函数，如  sqrt 。

**示例1：**

```
输入：num = 16
输出：true
```

**示例2：**

```
输入：num = 14
输出：false
```

## 题解思路

考虑到 $0 \leq x \leq num$ ，可用二分查找法来解决问题。

时间复杂度为 $O(\log 10)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
class Solution {
public:
    bool isPerfectSquare(int num) {
        int left = 0, right = num;
        while(right >= left){
            int half = left + (right - left) / 2;
            long square = (long)half * half;
            if(square < num){
                left = half + 1;
            }
            else if(square > num){
                right = half - 1;
            }
            else{
                return true;
            }
        }
        return false;
    }
};

```
