# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Input: l1 = [1,2,3], l2 = [4,5,6]
# Output: [5,7,9]
# Explanation: 321 + 654 = 975.
# 
# Input: l1 = [9], l2 = [9]
# Output: [8,1]

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0 # 
        dummy = ListNode(0, None)
        cur = dummy 

        while l1 or l2:
            curSum = carry 
            if not l1:
                curSum += l2.val
            elif not l2:
                curSum += l1.val
            else:
                curSum += (l1.val + l2.val)

            resVal = 0
            if curSum > 9:
                resVal = curSum % 10
                carry = 1
            else:
                resVal = curSum
                carry = 0

            cur.next = ListNode(resVal, None)
            l1 = l1.next if l1 else l1 
            l2 = l2.next if l2 else l2
            cur = cur.next

        
        if carry:
            cur.next = ListNode(carry, None)
            
        return dummy.next 
         
