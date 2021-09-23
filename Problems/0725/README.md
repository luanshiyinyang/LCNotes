## 题目描述

给你一个头结点为 head 的单链表和一个整数 k ，请你设计一个算法将链表分隔为 k 个连续的部分。

每部分的长度应该尽可能的相等：任意两部分的长度差距不能超过 1 。这可能会导致有些部分为 null 。

这 k 个部分应该按照在链表中出现的顺序排列，并且排在前面的部分的长度应该大于或等于排在后面的长度。

返回一个由上述 k 部分组成的数组。

**示例1：**

<img src='https://i.loli.net/2021/09/23/CfOTiaVY6s9Lzou.jpg'></img>

```
输入：head = [1,2,3], k = 5
输出：[[1],[2],[3],[],[]]
解释：
第一个元素 output[0] 为 output[0].val = 1 ，output[0].next = null 。
最后一个元素 output[4] 为 null ，但它作为 ListNode 的字符串表示是 [] 。
```

**示例2：**

<img src='https://i.loli.net/2021/09/23/ANIoQnG9HLO82Te.jpg'></img>

```
输入：head = [1,2,3,4,5,6,7,8,9,10], k = 3
输出：[[1,2,3,4],[5,6,7],[8,9,10]]
解释：
输入被分成了几个连续的部分，并且每部分的长度相差不超过 1 。前面部分的长度大于等于后面部分的长度。
```

## 题解思路

要将链表均分，首先需要获取到链表的长度。然后，根据长度和 k 判断分隔链表的位置，再将链表分割成数组。

时间复杂度为$O(n)$，空间复杂度为$O(1)$。

代码如下，也可见 [solve.ts](./solve.ts)。

```typescript
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

const splitListToParts = (head: ListNode | null, k: number): Array<ListNode | null> => {
  const res: Array<ListNode | null> = new Array(k).fill(null)
  let length = 0
  let node = head
  while (node) {
    node = node.next
    length++
  }
  let n = Math.floor(length / k)
  let m = length % k
  let i = m > 0 ? n + 1 : n
  let partHead = head
  let j = 0
  node = head
  while (node) {
    if (i > 1) {
      i--
      node = node.next
    } else {
      m--
      i = m > 0 ? n + 1 : n
      let nextHead = node.next
      node.next = null
      res[j] = partHead
      partHead = nextHead
      node = nextHead
      j++
    }
  }
  return res
}

```
