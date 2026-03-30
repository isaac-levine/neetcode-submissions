# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # well how would you merge 2 sorted linked lists
        # have one pointer for each list and iteratively add one node to the list at a time 

        # O(1) space
        # O(n * k) time so you can do a full scan of k lists of size n 
        
        # what if you take two merge into one, take two merge into one, etc. kind of like merge sort? 
        # we know we have the ability to remove() and insert() 

        # if there's 1 or 0 lists, we do nothing
        if not lists or len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]

        # [[1,2,4],[1,3,5],[3,6]]

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) in range(len(lists)) else None
                mergedLists.append(self.mergeTwoLists(list1, list2))
            lists = mergedLists
        return lists[0]

    def mergeTwoLists(self, list1: List[Optional[ListNode]], list2: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode() 
        ptr = dummy

        while list1 and list2:
            if list1.val <= list2.val: # list1's value is smaller
                ptr.next = list1
                list1 = list1.next
            else:                      # list2's value is smaller
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next
        
        if list1:
            ptr.next = list1
        if list2:
            ptr.next = list2

        return dummy.next
