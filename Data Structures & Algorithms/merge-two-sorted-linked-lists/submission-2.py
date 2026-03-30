# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # recursive solution 
        # if not list1:
        #     return list2
        # elif not list2:
        #     return list1
        # elif list1.val < list2.val:
        #     rest = self.mergeTwoLists(list1.next, list2) 
        #     list1.next = rest
        #     return list1
        # else:
        #     rest = self.mergeTwoLists(list1, list2.next)
        #     list2.next = rest
        #     return list2

        # iterative solution 
        # ListNode() -> ListNode() -> 1 -> 1 -> 2 -> 4
        # iterative way
        dummy = ListNode() 
        res = dummy.next = ListNode()

        while list1 and list2:
            # figure out which one to add to res.next
            if list1.val < list2.val:
                rest = list1.next
                res.next = list1
                list1 = rest
            else:
                rest = list2.next
                res.next = list2
                list2 = rest
            res = res.next

        if not list2:
            res.next = list1
        if not list1:
            res.next = list2
        

        return dummy.next.next
