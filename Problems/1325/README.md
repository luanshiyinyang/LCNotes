## 题目描述

给你一棵以 root 为根的二叉树和一个整数 target ，请你删除所有值为 target 的 **叶子节点** 。

注意，一旦删除值为 target 的叶子节点，它的父节点就可能变成叶子节点；如果新叶子节点的值恰好也是 target ，那么这个节点也应该被删除。

也就是说，你需要重复此过程直到不能继续删除。

**示例1：**

<img src='./1325_1.png'>

```
输入：root = [1,2,3,2,null,2,4], target = 2
输出：[1,null,3,null,4]
解释：
上面左边的图中，绿色节点为叶子节点，且它们的值与 target 相同（同为 2 ），它们会被删除，得到中间的图。
有一个新的节点变成了叶子节点且它的值与 target 相同，所以将再次进行删除，从而得到最右边的图。
```

**示例2：**

<img src='./1325_2.png'>

```
输入：root = [1,3,3,3,2], target = 3
输出：[1,3,null,null,2]
```

**示例3：**

<img src='./1325_3.png'>

```
输入：root = [1,2,null,2,null,2], target = 2
输出：[1]
解释：每一步都删除一个绿色的叶子节点（值为 2）。
```

**示例4：**

```
输入：root = [1,1,1], target = 1
输出：[]
```

**示例5：**

```
输入：root = [1,2,3], target = 1
输出：[1,2,3]
```

## 题解思路

应删除的节点有两个条件：

* 节点的值等于 target 。
* 节点为叶子节点。

因此，遍历的顺序为从叶子节点向根遍历（后序遍历），用递归即可实现。

时间复杂度为$O(n)$，空间复杂度为$O(h)$，其中，$n$为节点个数，$h$为二叉树深度。

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

const removeLeafNodes = (root: TreeNode | null, target: number): TreeNode | null => {
  const remove = (root: TreeNode | null): TreeNode | null => {
    if (!root) return null
    root.left = remove(root.left)
    root.right = remove(root.right)
    if (root.val == target && !root.left && !root.right) return null
    else return root
  }
  const res = remove(root)
  return res
}

```

## 优化思路

//TODO

尾调用优化
