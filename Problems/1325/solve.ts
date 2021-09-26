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
