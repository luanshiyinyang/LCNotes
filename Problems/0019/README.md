## 题目描述

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

**示例1：**

![0019](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

```
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
```

**示例2：**

```
输入：head = [1], n = 1
输出：[]
```

**示例3：**

```
输入：head = [1,2], n = 1
输出：[1]
```

## 题解思路

双指针的思路，指针一指向头节点，指针二指向头节点后第 $n$ 个节点，两指针指向其后继，直至指针二为空，此时指针一即为倒数第 $n$ 个节点。

时间复杂度为 $O(n)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *node1 = head, *node2 = new ListNode(0 ,head), *res = node2;
        while (node1 != nullptr) {
            if (n <= 0) {
                node2 = node2->next;
            }
            n--;
            node1 = node1->next;
        }
        node2->next = node2->next->next;
        return res->next;
    }
};

```
