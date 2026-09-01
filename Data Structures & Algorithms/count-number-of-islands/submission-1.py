class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        icecount=0
        visited=set()
        r,c=len(grid),len(grid[0])

        def find(x,y):
            if x<0 or x>=r or y<0 or y>=c:
                return
            if grid[x][y]=="0":
                return
            else:
                grid[x][y]="0"
                find(x+1,y)
                find(x,y+1)
                find(x-1,y)
                find(x,y-1)
                return


        if len(grid)==0:
            return 0
        else:
            for i in range(r):
                for j in range(c):
                    
                    if grid[i][j]=="1":
                        find(i,j)
                        print(i,j)
                        icecount=icecount+1

        return icecount


        