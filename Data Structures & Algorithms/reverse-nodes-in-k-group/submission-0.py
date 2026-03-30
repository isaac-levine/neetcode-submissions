# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        groupPrev = dummy # we're always going to store one node right before our group

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break # no more room for a group of k
            
            groupNext = kth.next # one node right after our group

            # reverse the group
            prev, curr = kth.next, groupPrev.next 
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # these next 3 lines are probably the most complicated part of the problem
            tmp = groupPrev.next # initially stores the first node in our group
            groupPrev.next = kth # put kth at the beginning of this group
            groupPrev = tmp
        return dummy.next # return new head of the linked list

    
    # call get kth using groupPrev
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -=1 
        return curr


    



             


        