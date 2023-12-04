class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        ans = float('inf')

        for start in range(n):
            q = deque([(start, None)])
            dist = {
                start: 0
            }

            while q:
                at, p = q.popleft()

                for to in g[at]:
                    if to == p: continue
                    if to in dist:
                        ans = min(ans, dist[at] + dist[to] + 1)
                    else:
                        q.append((to, at))
                        dist[to] = dist[at]+1
        
        return ans if ans != float('inf') else -1

