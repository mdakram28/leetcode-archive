class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene: return 0

        if startGene not in bank:
            bank.append(startGene)
            start = len(bank)-1
        else:
            start = bank.index(startGene)
        

        if endGene not in bank:
            return -1
        else:
            end = bank.index(endGene)
        
        n = len(bank)
        graph = [[] for _ in range(n)]


        for i in range(n):
            for j in range(i+1, n):
                if sum(1 for c1, c2 in zip(bank[i], bank[j]) if c1 != c2) == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        visited = [False] * n
        q = Deque([start])
        visited[start] = True
        d = 0

        while q:
            d += 1
            for _ in range(len(q)):
                at = q.popleft()
                for to in graph[at]:
                    if not visited[to]:
                        if to == end: return d
                        visited[to] = True
                        q.append(to)

        return -1
