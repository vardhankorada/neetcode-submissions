class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        queue = [[root]]
        ans = []
        while queue:
            level = queue[0]
            if len(queue) == 1: queue = []
            else: queue = queue[1:]
            ans.append(level)
            temp = []
            for node in level:
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            if len(temp) > 0 : queue.append(temp)
        res = []
        for node_l in ans:
            temp = []
            for node in node_l: temp.append(node.val)
            res.append(temp)
        return res