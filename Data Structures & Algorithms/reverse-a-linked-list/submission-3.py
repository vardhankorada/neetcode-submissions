# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        back,after = head,head.next
        back.next = None
        while after:
            temp = after.next
            after.next = back
            back = after
            after = temp
        return back
        