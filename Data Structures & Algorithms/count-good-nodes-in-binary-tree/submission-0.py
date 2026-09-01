# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_count = 0
        def dfs(root,mu):
            print(root,mu)
            nonlocal good_count
            if not root: return
            if root.val >= mu: 
                good_count += 1
            dfs(root.left,max(mu,root.val))
            dfs(root.right,max(mu,root.val))
        dfs(root,root.val)
        return good_count