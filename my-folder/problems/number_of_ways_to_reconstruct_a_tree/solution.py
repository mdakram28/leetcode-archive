class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph = defaultdict(set)
        for n1, n2 in pairs:
            graph[n1].add(n2)
            graph[n2].add(n1)
        
        multi = False
        comps = Deque([list(graph.keys())])
        while comps:
            comp = comps.popleft()
            # print(f"{comp=}")
            if len(comp) == 1: continue

            # Find roots
            root = None
            for node in comp:
                if len(graph[node]) == len(comp)-1:
                    if root is None:
                        root = node
                    else:
                        multi = True
                        break
                        
            if root is None: return 0

            
            # Remove connections to root (Should separate graph into smaller components)
            for child in graph[root]:
                graph[child].remove(root)

            
            # Calculate next components
            seen = set()
            for node in comp:
                if node != root and node not in seen:
                    next_comp = [node]
                    seen.add(node)
                    for at in next_comp:
                        for to in graph[at]:
                            if to not in seen:
                                seen.add(to)
                                next_comp.append(to)
                    comps.append(next_comp)
                    

        return 1 + int(multi)
        
        





