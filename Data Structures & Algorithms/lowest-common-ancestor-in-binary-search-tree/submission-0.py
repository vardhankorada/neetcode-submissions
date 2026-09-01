# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_one,path_two = [],[]
        curr = root
        while curr:
            path_one.append(curr)
            if curr.val == p.val: break
            elif curr.val < p.val: curr = curr.right
            else: curr = curr.left
        curr = root
        while curr:
            path_two.append(curr)
            if curr.val == q.val: break
            elif curr.val < q.val: curr = curr.right
            else: curr = curr.left
        if len(path_one) < len(path_two): path_one,path_two = path_two,path_one
        # for n in path_one: print(n.val,end=",")
        # print()
        # for n in path_two: print(n.val,end=",")
        for i in range(len(path_two)):
            if path_one[i]!=path_two[i]: return path_one[i-1]
            elif i == len(path_two)-1: return path_two[-1]
        return None