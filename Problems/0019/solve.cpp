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
