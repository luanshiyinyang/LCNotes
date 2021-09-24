## 题目描述

多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。这些子列表也可能会有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。

给你位于列表第一级的头节点，请你扁平化列表，使所有结点出现在单级双链表中。

**示例1：**

```
输入：head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
输出：[1,2,3,7,8,11,12,9,10,4,5,6]
解释：

输入的多级列表如下图所示：

```

<img src='./flatten.png'>

```
扁平化后的链表如下图：
```

<img src='./flattened.png'>

**示例2：**

```
输入：head = [1,2,null,3]
输出：[1,3,2]
解释：

输入的多级列表如下图所示：

  1---2---NULL
  |
  3---NULL

```

**示例3：**

```
输入：head = []
输出：[]
```

**如何表示测试用例中的多级链表？**

以 **示例 1** 为例：

```
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
```

序列化其中的每一级之后：

```
[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
```

为了将每一级都序列化到一起，我们需要每一级中添加值为 null 的元素，以表示没有节点连接到上一级的上级节点。

```
[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
```

合并所有序列化结果，并去除末尾的 null 。

```
[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
```

## 题解思路

从示例的输入输出可以看出：扁平化处理，实际上就是对链表的深度遍历。我的思路是：先对链表进行深度遍历，再将结果放在数组中，然后，对数组中的节点进行处理，最后，返回 head。

时间复杂度为$O(n)$，空间复杂度为$O(n)$。

代码如下，也可见 [solve.ts](./solve.ts)。

```typescript
/**
 * Definition for node.
 * class Node {
 *     val: number
 *     prev: Node | null
 *     next: Node | null
 *     child: Node | null
 *     constructor(val?: number, prev? : Node, next? : Node, child? : Node) {
 *         this.val = (val===undefined ? 0 : val);
 *         this.prev = (prev===undefined ? null : prev);
 *         this.next = (next===undefined ? null : next);
 *         this.child = (child===undefined ? null : child);
 *     }
 * }
 */

const flatten = (head: Node | null): Node | null => {
  const res: Node[] = []
  const dfs = (node: Node | null): void => {
    if (!node) return
    res.push(node)
    dfs(node.child)
    dfs(node.next)
  }
  dfs(head)
  for (let i = 0; i < res.length; i++) {
    res[i].child = null
    res[i].next = res[i + 1] || null
    res[i].prev = res[i - 1] || null
  }
  return head
}

```
