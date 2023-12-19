/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* addTwo(struct ListNode* l1, struct ListNode* l2, int carryOn);
struct ListNode* addTwoNum(struct ListNode* l1, struct ListNode* l2, int carryOn);

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    return addTwoNum(l1, l2, 0);
}

/* recursive function that performs addition of two singly linked lists */
struct ListNode* addTwoNum(struct ListNode* l1, struct ListNode* l2, int carryOn) {

    struct ListNode* carry = NULL;
    if (carryOn) {
        carry = malloc(sizeof(struct ListNode));
        carry -> val = 1; 
        carry -> next = NULL;
    }

    // base cases
    if (!l1 && !l2) return carry;
    if (!l1) return addTwoNum(l2, carry, 0);
    if (!l2) return addTwoNum(l1, carry, 0); 

    // addition performed here
    struct ListNode* added = addTwo(l1, l2, carryOn);
    added -> next = addTwoNum(l1 -> next, l2 -> next, l1 -> val + l2 -> val + carryOn > 9);

    return added; 
}

/* function that performs the addition of two single nodes */
struct ListNode* addTwo(struct ListNode* l1, struct ListNode* l2, int carryOn) {

    struct ListNode* added = malloc(sizeof(struct ListNode));
    added -> val = (l1 -> val + l2 -> val + carryOn) % 10;
    added -> next = NULL; 

    return added;
}