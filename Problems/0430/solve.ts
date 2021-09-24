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
