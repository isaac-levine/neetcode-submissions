# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# head = [2,4,6,8] --> [2,8,4,6]
# head = [2,4,6,8,10] --> [2,10,4,8,6]

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next # remember that fast should start at head.nextk
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # take slow.next ONWARD and reverse it
        cur = slow.next
        slow.next = None # the way you split the linked list without deleting data is by pointing a pointer to nothing
        prev = None
        while cur: 
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        first, second = head, prev # prev is now the start of the second list to zip
        while second: 
            temp1, temp2 = first.next, second.next 
            first.next = second # 4->8-> 
            second.next = temp1
            # first --> second --> firstNext
            first = temp1 # 4 -> 
            second = temp2 # 8->6->
