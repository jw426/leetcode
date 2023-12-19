/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/* improved and iterative version taken from solutions */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {

    // step 1 & 2
    struct ListNode* head = NULL;
    struct ListNode* tail = NULL; 

    // step 3 & 4 & 5
    int carry = 0, sum, digit1, digit2; 
    while (l1 || l2 || carry) {

        digit1 = l1 ? l1 -> val : 0;
        digit2 = l2 ? l2 -> val : 0;
        sum = digit1 + digit2 + carry; 

        struct ListNode* cur = malloc(sizeof(struct ListNode));
        cur -> val = sum % 10; 
        cur -> next = NULL; 
        
        // first addition 
        if (!tail) {
            head = cur; 
            tail = cur; 
        }
        else {
            tail -> next = cur; 
            tail = tail -> next; 
        } 

        // reset values for next iteration 
        carry = sum >= 10; 
        l1 = l1 ? l1 -> next : NULL;
        l2 = l2 ? l2 -> next : NULL;
    }

    return head; 
}
