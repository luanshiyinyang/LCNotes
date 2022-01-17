## 题目描述
请实现copyRandomList函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个next指针指向下一个节点，还有一个random指针指向链表中的任意节点或者null。

**示例1**
```
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
```

## 题解思路
这条题目需要复制一个链表，链表中每个节点不仅有next还有random。直接返回head也是不可能行的。要是采用双指针的方法也是不行的，因为每个节点还有一个random指针，很可能指向后面尚未遍历到的节点。所以我们的解法是，先在原列表中复制一份链表，再将其random赋值，最后将其拆分出来，听起来比较抽象。

第一步：在每个节点后面复制一个跟自己值一样的节点，random指针先不复制。比如原链表为7-13-11-10-1，复制过后便是7-7-13-13-11-11-10-10-1-1。

第二步：跳着遍历当前列表的奇数位置的节点（这些便是原节点），然后若其random指针不空，则将其后面的节点的random指针赋值跟自己一样。

第三部：奇数位置的为原节点，偶数位置的为新建节点，将偶数位置的节点拆分出来。

代码如下，也可见[solve.py](solve.py)。

```python
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None: return None
        ori = head
        while head: # 第一步：赋值节点
            temp = Node(head.val)
            temp.next = head.next
            head.next = temp
            head = temp.next
        cur = ori
        while cur: # 第二步：赋值random指针
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        answer = ori.next
        new = ori.next
        while new.next != None: # 第三步：拆分出新建的节点
            new.next = new.next.next
            new = new.next
        return answer
```
