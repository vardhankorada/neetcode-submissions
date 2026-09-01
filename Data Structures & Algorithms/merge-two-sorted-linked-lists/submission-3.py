# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy,store = None,None
        while list1 or list2:
            curr1 = list1.val if list1 else 101
            curr2 = list2.val if list2 else 101
            if curr1 <= curr2:
                if not dummy: 
                    dummy = list1
                    store = dummy
                else: 
                    dummy.next = list1
                    dummy = dummy.next
                list1 = list1.next
            else:
                if not dummy: 
                    dummy = list2
                    store = dummy
                else: 
                    dummy.next = list2
                    dummy = dummy.next
                list2 = list2.next
        return store