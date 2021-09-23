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
