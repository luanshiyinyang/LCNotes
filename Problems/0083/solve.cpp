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
    ListNode *deleteDuplicates(ListNode *head)
    {
        ListNode *pre = new ListNode(INT_MAX, head), *res = pre;
        while (head != nullptr)
        {
            if (head->val == pre->val)
            {
                pre->next = head->next;
                head = pre->next;
            }
            else
            {
                pre = head;
                head = head->next;
            }
        }
        return res->next;
    }
};
