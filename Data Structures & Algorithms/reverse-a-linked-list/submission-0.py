# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if not curr or not curr.next: return curr
        prev,after = None,curr.next
        while after:
            curr.next = prev
            prev = curr
            curr = after
            after = after.next
        curr.next = prev
        return curr