# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        new_head = None
        new_curr = None
        while l1 or l2:
            val_one = l1.val if l1 else 0
            val_two = l2.val if l2 else 0
            tot = val_one + val_two + carry
            dig = tot%10
            carry = tot//10
            new_node = ListNode(dig)
            if not new_head:
                new_head = new_node
                new_curr = new_head
            else:
                new_curr.next = new_node
                new_curr = new_curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry != 0:
            new_curr.next = ListNode(carry)
        return new_head              