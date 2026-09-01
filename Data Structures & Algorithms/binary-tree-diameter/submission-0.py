# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = 0
        def dfs(root):
            nonlocal max_dia
            if not root: return 0
            lh,rh = dfs(root.left), dfs(root.right)
            max_dia = max(max_dia, lh+rh)
            return max(lh,rh)+1
        dfs(root)
        return max_dia