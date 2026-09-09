# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        nodes = [root]
        while nodes:
            top = nodes[0]
            if self.isSameTree(top,subRoot): return True
            nodes = nodes[1:] if len(nodes) > 1 else []
            if top.left: nodes.append(top.left)
            if top.right: nodes.append(top.right)
        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (not q and p): return False
        if (not p and not q): return True
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)