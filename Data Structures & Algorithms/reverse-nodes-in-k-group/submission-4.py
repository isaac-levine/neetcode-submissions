# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # Rules:
            # reverse the linked list in chunks of size k.
            # if there are fewer than k nodes left, leave the nodes as they are. 

        # Plan: 
            # [1, 2, 3,         4, 5, 6]             k = 3
            # break up the groups of k O(n)
            # keep a result linked list
            # every time you break up a group:
                # reverse it
                # add it to the result linked list

        dummy = ListNode()
        res_ptr = dummy

        # 1. break up the linked list into groups of size k
        cur_group_size = 0 
        groups = [] 
        cur_group_head = head # the start of the current group
        while head:
            temp = head.next 

            cur_group_size += 1

            # Break up the group and add it to the result
            if cur_group_size == k: 
                head.next = None # cut the tie 
                res_ptr.next = self.reverse_linked_list(cur_group_head) # add the reversed group to the res
                while res_ptr.next: # move the res pointer to the end
                    res_ptr = res_ptr.next

                cur_group_head = temp # move the group ptr to the next node, fine if None 
                cur_group_size = 0 # reset cur_group_size back to 0 

            head = temp
            
        res_ptr.next = cur_group_head # add any (unreversed) leftovers, fine if None

        return dummy.next

    # reverse linked list
    def reverse_linked_list(self, head: Optional[ListNode]):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev



        