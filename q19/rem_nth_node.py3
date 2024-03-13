# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # called function
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # entry point of ListNode
        hold = ListNode(next = head)
        self._removeNthFromEnd(hold, n)
        return hold.next

    # helper function 
    # that carries out the operation
    def _removeNthFromEnd(self, head: ListNode, n: int) -> int:

        if head:
            keep = self._removeNthFromEnd(head.next, n)
            if not keep:
                head.next = head.next.next

            return keep - 1

        return n