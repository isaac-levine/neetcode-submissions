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
            # store them in-memory O(n) mem
            # reverse each one O(n)
            # connect them back together from in-memory store O(n)

        dummy = ListNode()
        res_ptr = dummy


        # 1. break up the linked list into groups of size k
        cur_group_size = 0 
        groups = [] 
        cur_group_head = head # the start of the current group
        while head:
            print("head is now: ", head.val, " cur_group_head: ", cur_group_head.val if cur_group_head else "None")
            temp = head.next 

            cur_group_size += 1
            if cur_group_size == k: 
                print("cur_group_size == k. (", cur_group_size, "==", k, ")")
                # break up the group 
                head.next = None # cut the tie 
                print("broke up the list at ", head.val)
                res_ptr.next = self.reverse_linked_list(cur_group_head)
                while res_ptr.next:
                    res_ptr = res_ptr.next
                print("res_ptr is now: ", res_ptr.val)
                # groups.append(self.reverse_linked_list(cur_group_head)) # add this linked list to the groups 
                cur_group_head = temp # move the pointer to the next node, fine if None 
                cur_group_size = 0 # reset cur_group_size back to 0 
                print("cur_group_size reset back to ", cur_group_size)

            head = temp
            
        
        if cur_group_head:
            res_ptr.next = cur_group_head # if there's anything (unreversed) leftover, add it to the groups. 


        return dummy.next

    # reverse linked list (all the way to its edge)
    def reverse_linked_list(self, head: Optional[ListNode]):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev



        