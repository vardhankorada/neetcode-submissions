# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = None
        def inorder(root):
            nonlocal count,ans
            if not root: return
            if count == k: return
            inorder(root.left)
            count += 1
            if count == k: ans = root
            inorder(root.right)
        inorder(root)
        return ans.val