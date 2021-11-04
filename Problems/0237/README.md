## 题目描述

请编写一个函数，用于 **删除单链表中某个特定节点** 。在设计函数时需要注意，你无法访问链表的头节点 head ，只能直接访问 **要被删除的节点** 。

题目数据保证需要删除的节点 **不是末尾节点** 。

**示例1：**

![](https://i.loli.net/2021/11/04/c3wNOkLEZT9UBFW.jpg)

```
输入：head = [4,5,1,9], node = 5
输出：[4,1,9]
解释：指定链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9
```

**示例2：**

![](https://i.loli.net/2021/11/04/ToaFIgOzyiefvmW.jpg)

```
输入：head = [4,5,1,9], node = 1
输出：[4,5,9]
解释：指定链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9
```

**示例3：**

```
输入：head = [1,2,3,4], node = 3
输出：[1,2,4]
```

**示例4：**

```
输入：head = [0,1], node = 0
输出：[1]
```

**示例5：**

```
输入：head = [-3,5,-99], node = -3
输出：[5,-99]
```

## 题解思路

算是记录一下链表删除节点的另一种方法吧。当无法获取到被删除节点的前驱节点时，可把需要删除的节点替换成其后继。

时间复杂度为 $O(1)$ ，空间复杂度为 $O(1)$ 。

代码如下，也可见 [solve.cpp](./solve.cpp)。

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        *node = *node->next;
    }
};

```
