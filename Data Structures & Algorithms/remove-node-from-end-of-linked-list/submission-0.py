# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow,fast = head,head
        count = 0
        while count <=n-1: 
            fast = fast.next
            count += 1
        if fast:
            while fast.next:
                fast = fast.next
                slow = slow.next
        else: return head.next
        if slow.next: slow.next = slow.next.next
        return head