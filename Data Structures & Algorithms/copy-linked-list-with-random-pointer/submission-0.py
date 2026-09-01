"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        store = {}
        curr = head
        new_head = None
        new_curr = None
        while curr:
            new_node = Node(curr.val)
            if not new_head: 
                new_head = new_node
                new_curr = new_head
            else: 
                new_curr.next = new_node
                new_curr = new_curr.next
            store[curr] = new_node
            curr = curr.next
        for key,value in store.items():
            node_one,node_two = key,value
            random_one = node_one.random
            if not random_one: continue
            node_two.random = store[random_one]
        return new_head
