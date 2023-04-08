class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        heap = []
        q = Deque()
        i = 0
        n = len(points)

        # x_offset = max(-min(p[0] for p in points), 0)
        # if x_offset:
        #     for p in points:
        #         p[0] += x_offset
        # print(points)

        q.append(points[0])
        heapq.heappush(heap, (-(points[0][0] + points[0][1]), points[0][0]))
        i += 1

        # while i<n and (points[i][0]-q[0][0]) <= k:
        #     x, y = points[i]
        #     q.append(points[i])
        #     heapq.heappush((-(x + y), x))
        #     i += 1
        
        max_val = -float('inf')

        # print(i, q, heap)


        while i<n or len(q)>1:
            # q.popleft()

            while i<n and (points[i][0]-q[0][0]) <= k:
                x, y = points[i]
                q.append(points[i])
                heapq.heappush(heap, (-(x + y), x))
                i += 1
            
            while heap and heap[0][1] <= q[0][0]:
                heapq.heappop(heap)

            if len(q) == 1:
                q.popleft()
                x, y = points[i]
                q.append(points[i])
                heapq.heappush(heap, (-(x + y), x))
                i += 1
                continue

            # print(i, q, heap, -heap[0][0] + (q[0][1] - q[0][0]))

            max_val = max(
                max_val,
                -heap[0][0] + (q[0][1] - q[0][0])
            )

            q.popleft()
            
        return max_val
        
