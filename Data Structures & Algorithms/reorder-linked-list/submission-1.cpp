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
    ListNode* reverseList(ListNode* head) {
        ListNode* curr = head;
        ListNode* prev = NULL;
        while (curr) {
            ListNode* nxt = curr->next;
            curr->next = prev;
            prev = curr;
            curr =nxt;
        }
        return prev;
    }
    void reorderList(ListNode* head) {
        ListNode *sec = head;
        ListNode *first = head;
        ListNode *fast = head;
        ListNode *prev = NULL;
        if (!head || !head->next) return;
        while (fast && fast->next ) {
            prev = sec;
            sec = sec->next;
            fast = fast->next->next;
        }
        if (fast) {
            prev = sec;
            sec = sec->next;
            prev->next = NULL;
        } else {
            if (prev) prev->next = NULL;
        }
        //printf("first->val:%d, sec->val:%d ",first->val,sec->val);
        ListNode* revSec = reverseList(sec);
        //printf(" revSec->val:%d , ",revSec->val);
        
        while (first && revSec) {
            ListNode *nf = first->next;
            first->next = revSec;
            ListNode *ns = revSec->next;
            revSec->next = nf;
            first = nf;
            revSec = ns;
        }
    }
};
