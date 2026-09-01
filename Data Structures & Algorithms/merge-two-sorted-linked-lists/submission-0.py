# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: return list2
        if list2 is None: return list1
        dummy = None
        store = None
        while list1 or list2:
            val_one,val_two = list1.val if list1 else 101, list2.val if list2 else 101
            if val_one <= val_two:
                if dummy is None: 
                    dummy = list1
                    store = dummy
                    list1 = list1.next
                    dummy.next = None
                else:
                    dummy.next = list1
                    dummy = dummy.next
                    list1 = list1.next
                    dummy.next = None
            else:
                if dummy is None: 
                    dummy = list2
                    store = dummy
                    list2 = list2.next
                    dummy.next = None
                else:
                    dummy.next = list2
                    dummy = dummy.next
                    list2 = list2.next
                    dummy.next = None
        return store