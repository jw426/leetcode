import sys 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        head = ListNode(val=-sys.maxsize - 1)
        tail = head 

        while len(lists):

            # removing None values 
            lists = [lst for lst in lists if lst is not None]
            min_head = None
            min_idx = None
            
            for i in range(len(lists)):

                lst = lists[i]
                # repeating values (same values)
                while lst and lst.val == tail.val:
                    lists[i] = lst.next
                    lst.next = None
                    tail.next = lst
                    tail = lst
                    lst = lists[i]
                    
                if not lst:
                    continue

                # finding new value
                if not min_head:
                    min_head = lst
                    min_idx = i
                    continue

                # new smallest listnode is found
                if min_head.val > lst.val:
                    min_head = lst
                    min_idx = i

            if min_head: 
                lists[min_idx] = min_head.next
                min_head.next = None
                tail.next = min_head
                tail = min_head

        return head.next
    