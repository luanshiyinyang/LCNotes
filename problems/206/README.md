## 题目描述

给定如下定义的单链表的头节点`head`，将该链表反转并返回反转后的头节点。

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## 题解思路

这题比较简单，有两个常见解法，分别为递归法和循环法，**考虑到便于代码的阅读和理解，我这里采用的是循环法**。它的思路其实很简单，如下图所示，从当前节点来考虑其实只需要保证能找到原来顺序的下一个节点，并将当前处理的前后两个的链接反向即可，这就需要一个变量记录下一个节点，另一个变量维护上一个节点构成的链表。

![](https://i.loli.net/2021/08/14/bQIDYZfyS32No8m.png)

完整代码如下，也可见[solve.py](./solve.py)。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, next = None, None
        while head is not None:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre
```

