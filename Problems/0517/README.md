## 题目描述

假设有 n 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。

在每一步操作中，你可以选择任意 m (1 <= m <= n) 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。

给定一个整数数组 machines 代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的 最少的操作步数 。如果不能使每台洗衣机中衣物的数量相等，则返回 -1 。

**示例1：**

```
输入：machines = [1,0,5]
输出：3
解释：
第一步:    1     0 <-- 5    =>    1     1     4
第二步:    1 <-- 1 <-- 4    =>    2     1     3    
第三步:    2     1 <-- 3    =>    2     2     2   
```

**示例2：**

```
输入：machines = [0,3,0]
输出：2
解释：
第一步:    0 <-- 3     0    =>    1     2     0    
第二步:    1     2 --> 0    =>    1     1     1     
```

**示例3：**

```
输入：machines = [0,2,0]
输出：-1
解释：
不可能让所有三个洗衣机同时剩下相同数量的衣物。
```

## 题解思路

这道题做的时候没有什么思路，看到别人的题解才写出来。思路总结起来主要是以下两点：

* 最小移动次数即为 **所有机器的最小运输衣服数量中的最大值**。
* 最小运输衣服数量 = 起始左边衣服总量与最终左边衣服总量的差值 + 起始右边衣服总量与最终右边衣服总量的差值。

时间复杂度为$O(n)$，空间复杂度为$O(1)$。

代码如下，也可见 [solve.ts](./solve.ts)。

```typescript
const findMinMoves = (machines: number[]): number => {
  let count = 0
  const clothesNum = machines.reduce((pre, cur) => pre + cur)
  if (clothesNum % machines.length) return -1
  const avg = clothesNum / machines.length
  let preSum = 0
  let backSum = clothesNum - machines[0]
  for (let i = 0; i < machines.length; i++) {
    count = Math.max(count, Math.max(i * avg - preSum, 0) + Math.max((machines.length - i - 1) * avg - backSum, 0))
    preSum += machines[i]
    backSum -= machines[i + 1]
  }
  return count
}

```
