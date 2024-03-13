/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {

    struct ListNode hold; 
    hold.next = head; 

    _removeNthFromEnd(&hold, n);
    return (hold.next); 
}

int _removeNthFromEnd(struct ListNode* head, int n) {

    // base case definition    
    // parse to end of list
    if (head) {
        // need to remove the next node
        int keep = _removeNthFromEnd(head -> next, n);
        if (!keep) {
            head -> next = head -> next -> next; 
        } 
        return keep - 1; 
    }
    
    return n;
}