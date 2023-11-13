class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        nodeid = {}
        nodes = list(set([t[0] for t in tickets] + [t[1] for t in tickets]))
        nodes.sort()
        n = len(nodes)
        for at, name in enumerate(nodes):
            nodeid[name] = at
        # print(list(enumerate(nodes)))
        g = [[0]*n for _ in range(n)]
        for a, b in tickets:
            g[nodeid[a]][nodeid[b]] += 1

        prev = []
        def isvalid(at):
            # nonlocal n
            prev.append(at)
            if len(prev) == len(tickets)+1:
                return True
            for to, remtickets in enumerate(g[at]):
                if remtickets == 0: continue
                g[at][to] -= 1
                if isvalid(to):
                    return True
                g[at][to] += 1
            prev.pop()
            return False
        
        isvalid(nodeid["JFK"])
        return [nodes[at] for at in prev]