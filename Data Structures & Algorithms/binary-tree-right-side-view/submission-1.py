# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        level = [root]
        temp = []
        while len(level) > 0:
            node = level[0]
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right)
            if len(level) > 1: level = level[1:]
            else: 
                ans.append(node.val)
                level = temp
                temp = []
        return ans

