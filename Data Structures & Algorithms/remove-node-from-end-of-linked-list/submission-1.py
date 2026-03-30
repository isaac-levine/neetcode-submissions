# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# head=[1,2,3,4]
# n=2

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
        if not head:
            return None
        
        # 1. reverse the linked list
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # [4,3,2,1]
        # now prev is the head of the reversed linked list
        # 2. iterate through the linked list to find the target node
        cur = prev # 4 
        headOfReversed = prev # 4
        prev = None 
        while n > 1: # n = 1 
            prev = cur # 4
            cur = cur.next # 3
            n -= 1

        # now cur should end at the target 
        # 3. remove the target node and repair connections
        target = cur 
        nextNode = cur.next
        if prev:
            prev.next = nextNode
        else:
            headOfReversed = nextNode

        # 4. reverse the resulting linked list
        cur = headOfReversed
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # 5. return the head 
        return prev
