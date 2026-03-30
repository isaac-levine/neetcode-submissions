# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        # first question: how do you find the nth node in the linked list? 
        # A: establish a lead of n + 1 between l and r, and then bump them over both one by one until r is off the edge (None) 


        # then you just remove it and return head 

        dummy = ListNode(0, head) 
        l = r = dummy 
        while n >= 0:
            r = r.next
            n -= 1
        

        while r:
            l = l.next
            r = r.next

        l.next = l.next.next

        return dummy.next
