# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    # recursive solution that only takes in
    # two nodes at once
    def swapPairs(self, head):
        
        # less than two items 
        # base case
        if not (head and head.next):
            return head 
        
        
        temp = head.next 
        head.next = self.swapPairs(head.next.next)
        temp.next = head 
        return temp 

        



