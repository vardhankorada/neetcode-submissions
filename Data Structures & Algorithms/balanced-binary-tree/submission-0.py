# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True
        def dfs(root):
            nonlocal flag
            if not root or not flag: return 0
            lh,rh = dfs(root.left),dfs(root.right)
            if abs(lh-rh)>1: flag = False
            return 1+max(lh,rh)
        dfs(root)
        return flag