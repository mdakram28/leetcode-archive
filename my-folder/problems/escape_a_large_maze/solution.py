class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:

        def make_maps(points):
            vals = set()
            for val in points:
                if val > 0 and val < 999999:
                    vals.add(val)
                    vals.add(val-1)
                    vals.add(val+1)
            vals.add(0)
            vals.add(999999)
            vals = list(vals)
            vals.sort()
            xmap = {}
            for i, x in zip(count(0), vals):
                xmap[x] = i
            return xmap
        
        xmap = make_maps([x for x, y in blocked] + [source[0], target[0]])
        ymap = make_maps([y for x, y in blocked] + [source[1], target[1]])

        blocked = set((xmap[x], ymap[y]) for x, y in blocked)
        source = (xmap[source[0]], ymap[source[1]])
        target = (xmap[target[0]], ymap[target[1]])
        maxx = xmap[999999]
        maxy = ymap[999999]

        # print(f"{blocked=}, {source=}, {target=}, {maxx=}, {maxy=}")

        visited = set()
        q = [source]
        visited.add(source)

        for x,y in q:
            if (x,y) == target:
                return True
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny = x+dx, y+dy
                if nx < 0 or nx > maxx or ny < 0 or ny > maxy:
                    continue
                if (nx, ny) in blocked or (nx, ny) in visited: continue
                visited.add((nx, ny))
                q.append((nx, ny))

        return False

