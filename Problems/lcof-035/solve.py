# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None: return None
        ori = head
        while head:
            temp = Node(head.val)
            temp.next = head.next
            head.next = temp
            head = temp.next
        cur = ori
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        answer = ori.next
        new = ori.next
        while new.next != None:
            new.next = new.next.next
            new = new.next
        return answer