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
