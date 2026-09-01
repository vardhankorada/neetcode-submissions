# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is None or head.next is None: return head
        # prev,curr,aft = None,head,head.next
        # while aft:
        #     curr.next = prev
        #     prev = curr
        #     curr = aft
        #     aft = aft.next if aft else None
        # curr.next = prev
        # return curr

        if head is None or head.next is None: return head
        prev,curr = None,head
        while curr.next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr.next = prev
        return curr