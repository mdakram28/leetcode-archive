class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = [[] for i in range(n)]

        for n1, n2, t in times:
            edges[n1-1].append((n2-1, t))
        
        min_times = [100_000_000] * n
        q = [k-1]
        min_times[k-1] = 0

        for node in q:
            curr = min_times[node]
            for to, t in edges[node]:
                if (curr+t) < min_times[to]:
                    min_times[to] = curr+t
                    q.append(to)
        
        max_time = max(min_times)
        return max_time if max_time != 100_000_000 else -1