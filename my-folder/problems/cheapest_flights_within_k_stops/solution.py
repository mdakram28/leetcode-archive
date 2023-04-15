class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        INF = float('inf')
        price = [INF] * n
        graph = [[] for _ in range(n)]

        for i in range(len(flights)):
            graph[flights[i][0]].append(i)

        q = [(0, src)]
        next_q = []
        price[src] = 0

        for _ in range(k+1):
            next_q.clear()
            q.sort()
            for p0, at in q:
                for f in graph[at]:
                    to = flights[f][1]
                    p = flights[f][2] + p0
                    if p < price[to]:
                        price[to] = p
                        next_q.append((p, to))
            q, next_q = next_q, q
        return price[dst] if price[dst] != INF else -1