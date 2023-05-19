class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n

        # def check_node(at, c):
        #     if color[at]:
        #         return color[at] == c
        #     color[at] = c
        #     c = 3-c
        #     for to in graph[at]:
        #         if not check_node(to, c):
        #             return False
        #     return True
        
        q = []
        qi = 0

        for i in range(n):
            if color[i]: continue

            q.append(i)
            color[i] = 1

            while qi < len(q):
                at = q[qi]
                qi += 1
                c = 3-color[at]
                for to in graph[at]:
                    if color[to]:
                        if color[to] != c: return False
                    else:
                        color[to] = c
                        q.append(to)
        
        return True

            