## 题目描述

给定平面上 n 对互不相同的点 points ，其中 points[i] = [xi, yi] 。回旋镖是由点 (i, j, k) 表示的元组，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

返回平面上所有回旋镖的数量。

**示例 1：**
```
输入：points = [[0,0],[1,0],[2,0]]
输出：2
解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
```
**示例 2：**
```
输入：points = [[1,1],[2,2],[3,3]]
输出：2
```
**示例 3：**
```
输入：points = [[1,1]]
输出：0
```

## 题解思路

这道题想了挺久，除了枚举法也没想到其他好的解法了，大概看了看题解的标题，也基本上都是暴力求解法，于是就直接按照自己的想法开始做了。思路是：遍历每个点，然后求出该点与其他点的距离，并放在哈希表中，哈希表的 key 为距离的值，哈希表 value 为对应 key 的个数，结果就是每个点所有$2*C_{value}^2$的和。时间复杂度为$O(n^2)$，空间复杂度为$O(n)$。

代码如下，也可见 [solve.ts](./solve.ts)。

```typescript
const numberOfBoomerangs = (points: number[][]): number => {
  const distanceMap = new Map<number, number>()
  let res = 0
  for (const i of points) {
    for (const j of points) {
      const distance = (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2
      distanceMap.set(distance, ~~distanceMap.get(distance) + 1)
    }
    for (const value of distanceMap.values()) {
      res += value * (value - 1)
    }
    distanceMap.clear()
  }
  return res
}
```