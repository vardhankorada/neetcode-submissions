# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_p = self.find_path(root,p)
        path_q = self.find_path(root,q)
        for ind in range(0,min(len(path_p),len(path_q))):
            if path_p[ind] != path_q[ind]: return path_p[ind-1]
        return path_p[-1] if len(path_p) < len(path_q) else path_q[-1]

    def find_path(self,root,node):
        curr = root
        path = []
        while curr != node:
            path.append(curr)
            if curr.val > node.val: curr = curr.left
            else: curr = curr.right
        path.append(node)
        return path
