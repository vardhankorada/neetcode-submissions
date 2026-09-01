# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = [[root]]
        while len(queue[-1]) > 0:
            level = queue[-1]
            new_level = []
            for node in level:
                if node.left: new_level.append(node.left)
                if node.right: new_level.append(node.right)
            queue.append(new_level)
        return [level[-1].val for level in queue[:len(queue)-1]]