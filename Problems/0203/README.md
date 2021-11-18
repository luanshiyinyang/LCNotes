## 题目描述

给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 **新的头节点** 。

**示例1：**

![0203](https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg)

```
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]
```

**示例2：**

```
输入：head = [], val = 1
输出：[]
```

**示例3：**

```
输入：head = [7,7,7,7], val = 7
输出：[]
```

## 题解思路

遍历链表，若 Node.val ！= val 则将其插入到新链表中。

时间复杂度为 $O(n)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
    ListNode *removeElements(ListNode *head, int val)
    {
        ListNode *newHead = new ListNode(-1);
        ListNode *res = newHead;
        while (head != nullptr)
        {
            if (head->val == val)
            {
                newHead->next = nullptr;
                head = head->next;
                continue;
            }
            newHead->next = head;
            head = head->next;
            newHead = newHead->next;
        }
        return res->next;
    }
};

```
