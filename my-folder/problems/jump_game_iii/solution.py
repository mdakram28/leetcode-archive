class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        
        q = Deque([start])
        visited[start] = True

        while q:
            at = q.popleft()
            if arr[at] == 0: return True

            if at + arr[at] < n and not visited[at + arr[at]]:
                visited[at + arr[at]] = True
                q.append(at + arr[at])
            
            if at - arr[at] >=0 and not visited[at - arr[at]]:
                visited[at - arr[at]] = True
                q.append(at - arr[at])
        
        return False