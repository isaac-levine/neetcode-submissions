# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# head=[1,2,3,4]
# n=2

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
        dummy = ListNode(0, head) 
        l, r = dummy, dummy

        # establish a lead of size n + 1 between the right and the left nodes 
        while n >= 0:
            r = r.next
            n -= 1


        # move both of them until r falls of the edge
        while r:
            l = l.next
            r = r.next
        
        # skip over the target, effectively deleting it 
        # beacause of the dummy node and there is another dummy node effecively at the end by design, you dont need to do a null check here
        l.next = l.next.next

        return dummy.next

        
