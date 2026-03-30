# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]

        
        while len(lists) > 1:
            # take every two pairs of lists and merge them together 
            newLists = [] # the resulting list of linked-lists after merging all pairs together 
            for i in range(0, len(lists), 2):
                list1, list2 = lists[i], lists[i + 1] if (i + 1) < len(lists) else None
                mergedList = self.mergeTwoLists(list1, list2) 
                newLists.append(mergedList) 
            
            lists = newLists # keep going until there's only one merged list left

        return lists[0]

    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        while list1 and list2:
            if list1.val <= list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2) 
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2

        if not list1:
            return list2
        elif not list2:
            return list1
