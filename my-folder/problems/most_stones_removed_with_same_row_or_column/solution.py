class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        visited = [False] * len(stones)

        for i, [r,c] in enumerate(stones):
            rows[r].append(i)
            cols[c].append(i)

        def travel(at):
            if visited[at]: return
            visited[at] = True
            for to in rows[stones[at][0]]:
                travel(to)
            
            for to in cols[stones[at][1]]:
                travel(to)
        
        ans = 0
        for i in range(len(stones)):
            if not visited[i]:
                travel(i)
                ans += 1
                # print(f"Visiting {i}", visited)
        
        return len(stones) - ans