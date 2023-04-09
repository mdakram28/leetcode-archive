class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0] * len(rooms)

        q = Deque()
        q.append(0)

        while q:
            node = q.popleft()
            if visited[node]:
                continue
            visited[node] = 1
            for to in rooms[node]:
                if not visited[to]:
                    q.append(to)
        
        return sum(visited) == len(rooms)
