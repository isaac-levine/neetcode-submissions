# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # 0 -> 1 -> 2 -> 3 -> 4 -> None
        #           l               r
        # n=0
        
        # find the nth node from the end of the list 
        dummy = ListNode(0, head) 
        l = dummy
        r = head

        # establish an n + 1 sized lead between r and l 
        while n > 0 and r:
            r = r.next
            n -= 1

        # move them both until r is off the edge
        while r:
            l = l.next
            r = r.next 

        # l should be right before the node to remove
        l.next = l.next.next

        return dummy.next