class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m = len(forest)
        n = len(forest[0])
        INF = float('inf')

        if forest[0][0] == 0:
            return -1

        vals = []
        for r in range(m):
            for c in range(n):
                if forest[r][c] > 1:
                    vals.append((forest[r][c], r, c))
        vals.sort()
        # for r in range(m):
        #     for c in range(n):
        #         print(f"{vals.index((forest[r][c], r, c)) if forest[r][c] else '  ':2}", end='')
        #         print('|', end='')
        #     print()
        
        prev_r = 0
        prev_c = 0
        total_dist = 0
        q = []
        for val, next_r, next_c in vals:
            dist = [[INF] * n for r in range(m)]

            dist[prev_r][prev_c] = 0
            q.append(( 0, prev_r, prev_c))

            min_dist = INF

            while q:
                d, r, c = heapq.heappop(q)
                if r == next_r and c == next_c:
                    min_dist = min(min_dist, d)
                elif d >= min_dist:
                    continue
                d += 1
                for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or forest[nr][nc] == 0:
                        continue
                    if d < dist[nr][nc]:
                        dist[nr][nc] = d
                        heapq.heappush(q, (d, nr, nc))
            # print(f"Distance from {prev_r},{prev_c} -> {next_r},{next_c} = {min_dist}")
            if min_dist == INF:
                # print(dist)
                return -1
            total_dist += min_dist

            prev_r, prev_c = next_r, next_c

        return total_dist