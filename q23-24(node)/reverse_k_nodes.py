# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def recursiveReverse(self, node, n, k):
        
        # base case 1 
        if not node:
            return None, None

        # base case 2
        if n <= 1:
            nhead, _ = self.recursiveReverse(node.next, k, k)
            node.next = nhead
            return node, node

        head, tail = self.recursiveReverse(node.next, n-1, k)
        if not head and not tail:
            if n == k:
                return node, None
            else:
                return None, None

        node.next = tail.next
        tail.next = node
        return head, node

        
    def reverseKGroup(self, head, k):
        
        return self.recursiveReverse(head, k, k)[0]