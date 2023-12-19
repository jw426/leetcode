# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        tail = head
        carry = 0

        # ends when there are no values to be added or carry on values 
        while l1 is not None or l2 is not None or carry != 0:

            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0
            sm = digit1 + digit2 + carry

            # append the added result of the digits to solution
            added = ListNode(sm % 10)
            tail.next = added
            tail = tail.next 

            # reset values for next iteration 
            carry = sm // 10
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None 

        result = head.next
        head.next = None
        return result 


    