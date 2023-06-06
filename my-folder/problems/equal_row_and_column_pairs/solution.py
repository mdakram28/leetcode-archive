
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        root = {}

        for row in grid:
            node = root
            for val in row:
                node = node.setdefault(val, {})
            node["count"] = node.get('count', 0) + 1
        
        ans = 0
        for c in range(n):
            node = root
            for r in range(n):
                if grid[r][c] not in node: break
                node = node[grid[r][c]]
            else:
                ans += node["count"]
        
        return ans