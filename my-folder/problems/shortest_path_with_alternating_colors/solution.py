class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        dist_red = [float('inf')] * n
        dist_blue = [float('inf')] * n

        redGraph = defaultdict(set)
        blueGraph = defaultdict(set)

        for i, j in redEdges:
            redGraph[i].add(j)
        
        for i, j in blueEdges:
            blueGraph[i].add(j)

        # def dfs_red(at):
        #     dist = dist_blue[at] + 1
        #     for to in redGraph[at]:
        #         if dist_red[to] > dist:
        #             dist_red[to] = dist
        #             dfs_blue(to)
        
        # def dfs_blue(at):
        #     dist = dist_red[at] + 1
        #     for to in blueGraph[at]:
        #         if dist_blue[to] > dist:
        #             dist_blue[to] = dist
        #             dfs_red(to)
        
        dist_red[0] = 0
        dist_blue[0] = 0

        q = Deque([(0, True), (0, False)])
        d = 0

        while q:
            d += 1
            for _ in range(len(q)):
                at, fromRed = q.popleft()
                if fromRed:
                    for to in blueGraph[at]:
                        if d < dist_blue[to]:
                            dist_blue[to] = d
                            q.append((to, False))
                else:
                    for to in redGraph[at]:
                        if d < dist_red[to]:
                            dist_red[to] = d
                            q.append((to, True))
        
        ans = []
        for i in range(n):
            d = min(dist_red[i], dist_blue[i])
            ans.append(d if d != float('inf') else -1)
        
        return ans
                

