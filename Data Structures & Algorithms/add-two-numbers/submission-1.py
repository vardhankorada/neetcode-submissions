# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = None
        head = None
        while l1 or l2:
            if not l1: v1 = 0
            else: v1 = l1.val
            if not l2: v2 = 0
            else: v2 = l2.val
            val = carry + v1 + v2
            new = ListNode(val = val%10)
            carry = val//10
            if res: 
                res.next = new
                res = res.next
            else:
                res = new
                head = res
            if l1 : l1 = l1.next
            if l2: l2 = l2.next
        if carry != 0:
            res.next = ListNode(val=carry)
        return head
        