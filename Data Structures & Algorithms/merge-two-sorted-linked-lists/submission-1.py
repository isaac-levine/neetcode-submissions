# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val < list2.val:
            rest = self.mergeTwoLists(list1.next, list2) 
            list1.next = rest
            return list1
        else:
            rest = self.mergeTwoLists(list1, list2.next)
            list2.next = rest
            return list2

        
