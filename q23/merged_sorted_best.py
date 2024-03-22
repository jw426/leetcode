from collections import defaultdict 

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):

        valdict = defaultdict(int)
        
        for list in lists:
            cur = list
            while cur:
                valdict[cur.val] += 1
                cur = list.next 
        
        head = ListNode()
        tail = head
        for val, cnt in sorted(valdict.items()):
            for _ in range(cnt):
                tail.next = ListNode(val)
                tail = tail.next 

        return head.next

