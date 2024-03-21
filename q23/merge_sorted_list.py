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

        while lists:

            # removing None values 
            lists = [list for list in lists if list is not None]
            min_head = None
            
            for list in lists:

                # repeating values (same values)
                while list and list.val == head.val:
                    tail.next = list
                    tail = list
                    list = list.next

                # finding new value
                if not min_head:
                    min_head = list
                    continue

                # new smallest listnode is found
                if min_head.val > list.val:
                    min_head = list

            if min_head: 
                tail.next = min_head
                tail = min_head

        return head.next
    
obj = Solution()
res = obj.mergeKLists(lists = [[1,4,5],[1,3,4],[2,6]])
print(res)