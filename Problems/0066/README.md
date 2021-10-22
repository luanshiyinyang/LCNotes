## 题目描述

给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

**示例1：**

```
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
```

**示例2：**

```
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
```

**示例3：**

```
输入：digits = [0]
输出：[1]
```

## 题解思路

简单题，从尾部遍历数组，若值为 9 则前一个元素加 1 。

时间复杂度为$O(n)$，空间复杂度为$O(1)$。

代码如下，也可见 [solve.ts](./solve.ts)。

```typescript
const plusOne = (digits: number[]): number[] => {
  let n = 1
  for (let i = digits.length - 1; i >= 0 && n != 0; i--) {
    if (digits[i] == 9) digits[i] = 0
    else {
      digits[i]++
      n = 0
    }
  }
  if (n == 1) digits.unshift(1)
  return digits
}

```
