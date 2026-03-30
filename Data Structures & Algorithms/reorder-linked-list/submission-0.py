# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        # 2 -> 4 -> 6 -> 8

        # take the forward and the reverse, and zip them together alternating 

        # fast and slow pointer strategy to find halfway point (when fast reaches the end)   

        # 1. find the middle
        slow, fast = head, head.next 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
       
        
        # 2. reverse the second half of the list
        second = slow.next
        slow.next = None # break the link between the two halves
        prev = None 
        while second:
            temp = second.next 
            second.next = prev
            prev = second 
            second = temp
        
        # 3. zip/merge them together
        second = prev # the old 'second' is going to be null at this point, so we use prev
        first = head
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            # shift our pointers
            first = temp1
            second = temp2

        # dont need to return anything
