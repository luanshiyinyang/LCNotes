## 题目描述

符合下列属性的数组 arr 称为 山峰数组（山脉数组） ：

* arr.length >= 3
* 存在 i（0 < i < arr.length - 1）使得：
  * arr[0] < arr[1] < ... arr[i-1] < arr[i]
  * arr[i] > arr[i+1] > ... > arr[arr.length - 1]

给定由整数组成的山峰数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i ，即山峰顶部。

**示例1：**

```
输入：arr = [0,1,0]
输出：1
```

**示例2：**

```
输入：arr = [1,3,5,4,2]
输出：2
```

**示例3：**

```
输入：arr = [0,10,5,2]
输出：1
```

**示例4：**

```
输入：arr = [3,4,5,1]
输出：2
```

**示例5：**

```
输入：arr = [24,69,100,99,79,78,67,36,26,19]
输出：2
```

## 题解思路

典型的分治法题目，山顶左边单调递增，山顶右边单调递减，思路等同二分查找法。

时间复杂度为$O(\log(n))$，空间复杂度为$O(1)$。

代码如下，也可见 [solve.ts](./solve.ts)。

```typescript
const peakIndexInMountainArray = (arr: number[]): number => {
  let start = 0
  let end = arr.length - 1
  let half = Math.ceil(start + (end - start) / 2)
  while (half > 0 && half < arr.length - 1) {
    if (arr[half - 1] < arr[half] && arr[half] > arr[half + 1]) break
    else if (arr[half + 1] > arr[half]) {
      start = half
      half = Math.ceil(start + (end - start) / 2)
    } else if (arr[half - 1] > arr[half]) {
      end = half
      half = Math.ceil(start + (end - start) / 2)
    }
  }
  return half
}

```
