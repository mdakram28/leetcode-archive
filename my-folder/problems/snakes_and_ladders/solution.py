class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        # board = [max(, 0) for i in range(n*n)]
        # graph = [[] for i in range(n*n)]

        # def node_dest(i):

        # i = 0
        # for r in range(n-1, -1, -1):
        #     for c in (range(n) if (n-1-r)%2==0 else range(n-1, -1, -1)):
        #         dest = board[r][c]-1 if board[r][c] > 0 else i
        #         for j in range(max(i-6, 0), i):
        #             graph[j].append(dest)
        #         i += 1

        inf = float('inf')
        dist = [inf]*(n*n)

        q = Deque()
        q.append(0)
        dist[0] = 0

        while q:
            i = q.popleft()
            d = dist[i] + 1
            for j in range(i+1, min(i+7, n*n)):
                to = board[n-1-j//n][j%n if (j//n)%2==0 else n-1-j%n]-1
                if to < 0:
                    to = j
                if d < dist[to]:
                    dist[to] = d
                    q.append(to)
        
        return dist[-1] if dist[-1] != inf else -1
