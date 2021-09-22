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
