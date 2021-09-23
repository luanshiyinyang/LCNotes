## 题目描述

给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。

**示例1：**

```
输入: root = [1,3,2,5,3,null,9]
输出: [1,3,9]
解释:
          1
         / \
        3   2
       / \   \  
      5   3   9 
```

**示例2：**

```
输入: root = [1,2,3]
输出: [1,3]
解释:
          1
         / \
        2   3
```

**示例3：**

```
输入: root = [1]
输出: [1]
```

**示例4：**

```
输入: root = [1,null,2]
输出: [1,2]
解释:      
           1 
            \
             2    
```

**示例5：**

```
输入: root = []
输出: []
```

## 题解思路

层次遍历二叉树，用一个变量保存该层最后一个不为 null 的节点，另一个变量保存该层遍历到目前为止最大值。当从队列出来的节点等于该层最后一个节点时，即代表该层遍历结束，将最大值加到返回数组中去，并将最大值赋值成数值最小值。直到队列为空，遍历完成。

时间复杂度为$O(n)$，空间复杂度为$O(n)$。

代码如下，也可见 [solve.ts](./solve.ts)。

```typescript
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

const largestValues = (root: TreeNode | null): number[] => {
  const res: number[] = []
  const queue: TreeNode[] = []
  if (!root) return res
  queue.push(root)
  let max = -Number.MAX_VALUE
  let lastNode: TreeNode = root
  while (queue.length > 0) {
    let node = queue.shift()
    max = Math.max(max, node.val)
    node.left && queue.push(node.left)
    node.right && queue.push(node.right)
    if (node == lastNode) {
      res.push(max)
      max = -Number.MAX_VALUE
      lastNode = queue[queue.length - 1]
    }
  }
  return res
}

```
