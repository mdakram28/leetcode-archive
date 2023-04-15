class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {}
        extra = None
        for n1, n2 in edges:
            if n2 in parent:
                extra = n1, n2
            else:
                parent[n2] = n1
        
        if extra:
            node = parent[extra[1]]
            while node in parent and node != extra[1]:
                node = parent[node]
            if node in parent:
                return parent[extra[1]], extra[1]
            else:
                return extra


        node = 1
        visited = {}
        st = []
        while node not in visited:
            visited[node] = len(st)
            st.append(node)
            node = parent[node]
        
        for node in st[:visited[node]]:
            del visited[node]
        
        # print(st, node, visited)

        for n1, n2 in edges[::-1]:
            if n1 in visited and n2 in visited:
                return n1, n2
        
        return None