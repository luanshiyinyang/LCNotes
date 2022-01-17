## 题目描述

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

**示例1：**

```
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```

## 题解思路

这道题的难度是Easy，本题也非常简单，算是链表类型题和双指针类型题里面非常基础的一道题，但是我还是把这道题的题解记录了下来，因为这题有很多链表类题目应该注意的细节，比如**空头节点初始化**、**双链表的遍历条件**、**尾部节点的更新**等，这些是我们构思和实现时往往区别的鸿沟，也就是很多人所说的 **“我能想出大致的解法，但我实现出来总是差点什么”** 。

回到本题上来，这题其实非常的简单，引入伪头节点，然后利用双指针分别从头到尾遍历两个链表即可，算法流程如下。

1. 初始化伪头节点head0，将当前节点curr指向他；
2. 当两个链表均不为空时，将当前节点curr下一个位置指向值较小的那个链表节点，对应链表同时向后遍历；
3. 当其中一个链表为空后，将伪头节点指向剩余的非空链表。

本题的代码如下，也可见于[solve.py](./solve.py)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head0 = curr = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next, l1 = l1, l1.next
            else:
                curr.next, l2 = l2, l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return head0.next
```

上述解法的时间复杂度为$O(M+N)$，其中$M$和$N$分别为链表l1合l2的长度，合并操作需遍历两链表。空间复杂度为$O(1)$，伪头节点占用常数级别的额外空间。