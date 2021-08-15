## 题目描述

给定如下定义的两个有序单链表的头节点，试着将两个链表合并为一个有序链表。

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## 题解思路

这题也比较简单，核心思路是采用递归的方法，比较当前两个链表的头节点值得大小，将较小的那个作为合并后的链表的头节点，将其指向的后续节点所组成的链表和另一个较大节点组成的链表继续进行上述合并步骤，并将结果和当前较小的节点链接起来。递归的终止条件是其中一个链表为空时，返回另一个链表的头节点即可。如下图所示，蓝绿黄就代表递归调用合并函数的顺序。

![](https://i.loli.net/2021/08/15/GDwQsK9n5qW3Zzk.png)


完整代码如下，也可见[solve.py](./solve.py)。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```

