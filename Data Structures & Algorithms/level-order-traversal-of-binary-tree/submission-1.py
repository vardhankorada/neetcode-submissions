class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = [[root]]
        while len(queue[-1]) > 0:
            level = queue[-1]
            new_level = []
            for node in level:
                if node.left: new_level.append(node.left)
                if node.right: new_level.append(node.right)
            queue.append(new_level)
        return [[node.val for node in level] for level in queue[:len(queue)-1]]