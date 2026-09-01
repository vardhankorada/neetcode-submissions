# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_one,path_two = self.makeDFSPath(root,p),self.makeDFSPath(root,q)
        if len(path_one) < len(path_two): path_one,path_two = path_two,path_one
        for i in range(len(path_two)):
            if path_one[i]!=path_two[i]: return path_one[i-1]
            elif i == len(path_two)-1: return path_two[-1]
        return None
    def makeDFSPath(self,root,node):
        curr,path = root,[]
        while curr:
            path.append(curr)
            if curr.val == node.val: break
            elif curr.val < node.val: curr = curr.right
            else: curr = curr.left
        return path