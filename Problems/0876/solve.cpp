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
    ListNode* middleNode(ListNode* head) {
        ListNode node = head;
        int count = 0;
        while (!head) {
            if (count % 2 == 0) {
                node = node->next;
            }
            head = head->next;
            count++;
        }
        return node;
    }
};
