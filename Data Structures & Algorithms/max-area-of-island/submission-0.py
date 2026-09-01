class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == 0
            ):
                return 0
            grid[r][c] = 0
            tot = 1
            for dr, dc in directions:
                tot += dfs(r + dr, c + dc)
            return tot
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    ans = max(ans,dfs(r, c))
        
        return ans