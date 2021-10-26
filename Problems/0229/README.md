## 题目描述

给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

**示例1：**

```
输入：[3,2,3]
输出：[3]
```

**示例2：**

```
输入：nums = [1]
输出：[1]
```

**示例3：**

```
输入：[1,1,1,3,3,2,2,2]
输出：[1,2]
```

## 题解思路

最先想到的是用哈希表来解决该问题，这里想记录一下摩尔投票法。

> 首先请考虑最基本的摩尔投票问题，找出一组数字序列中出现次数大于总数 $\frac{1}{2}$ 的数字（并且假设这个数字一定存在）。显然这个数字只可能有一个。摩尔投票算法是基于这个事实：每次从序列里选择两个不相同的数字删除掉（或称为“抵消”），最后剩下一个数字或几个相同的数字，就是出现次数大于总数一半的那个。

同理出现次数大于总数 $\frac{1}{3}$ 的数字也最多存在两个，具体做法如下：

* 用变量 num1 和 num2 表示两个可能为结果的值，变量 vote1 和 vote2 表示对应 num1 和 num2 的剩余个数。遍历 nums ，若与 num1 或 num2 相等，则 对应剩余个数加 1 ，否则，删除这三个不相同的数， vote1 和 vote2 都减 1 。

* 检测 num1 和 num2 是否为出现次数大于总数 $\frac{1}{3}$ 的数字。若是，则添加到结果数组中。

时间复杂度为 $O(n)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.ts](./solve.ts)。

```typescript
const majorityElement = (nums: number[]): number[] => {
  let num1 = 0
  let num2 = 0
  let vote1 = 0
  let vote2 = 0
  let count1 = 0
  let count2 = 0
  const res = []
  for (const num of nums) {
    if (num1 == num) vote1++
    else if (num2 == num) vote2++
    else if (vote1 == 0) {
      num1 = num
      vote1++
    } else if (vote2 == 0) {
      num2 = num
      vote2++
    } else {
      vote1--
      vote2--
    }
  }
  for (const num of nums) {
    if (num == num1) count1++
    else if (num == num2) count2++
  }
  if (count1 > nums.length / 3) res.push(num1)
  if (count2 > nums.length / 3) res.push(num2)
  return res
}

```
