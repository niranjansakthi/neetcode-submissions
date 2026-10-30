from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1
            
        queue = deque([(0, 0, 1)]) # (row, col, path_length)
        visited = set([(0, 0)])
        
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        
        while queue:
            r, c, length = queue.popleft()
            
            if r == rows - 1 and c == cols - 1:
                return length
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, length + 1))
                    
        return -1