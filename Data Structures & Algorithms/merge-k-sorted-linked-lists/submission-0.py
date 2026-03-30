# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
       
        # K*N is bad
        # Merge sort approach --> divide and conquer 
            # can do O(N * log K) --> do log k number of merges

        

        if not lists or len(lists) == 0:
            return None

        # Take pairs of linked lists and merge them until there's only one left, and that's our output
        while len(lists) > 1:
            mergedList = []
            # get pairs of linked lists (l1, l2)
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedList.append(self.mergeTwoLists(l1, l2)) # merge them

            lists = mergedList

        return lists[0]

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = node = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next
                node = node.next

            node.next = list1 or list2

            return dummy.next

        

