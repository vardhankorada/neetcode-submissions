# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = [[root]]
        queue = [root]
        temp = []
        while len(queue) > 0:
            node = queue[0]
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right)
            if len(queue) > 1: queue = queue[1:]
            else: 
                if len(temp) > 0: ans.append(temp)
                queue = temp
                temp = []
        for li in ans:
            for i in range(len(li)): li[i] = li[i].val
        return ans
        