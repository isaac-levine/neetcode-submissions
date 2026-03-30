# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0, 1, 2, 3, 4, 5, 6] --> [0, 6, 1, 5, 2, 4, 3]
        # [2,4,6,8] -> [2,8,4,6]
        # [2,4,6,8,10] -> [2,10,4,8,6]


        # 1.) find the middle 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # slow will be at the halfway point

        # 2.) reverse the second half
        # reverse the linked list that starts at second.next
        cur = slow.next
        slow.next = None # break the line between the two halves 
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp


        # 3.) merge them 
        # prev is the head of the reversed list 
        first, second = head, prev
        ptr = head
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            # shift our pointers
            first = temp1 
            second = temp2

