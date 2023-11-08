class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        visited = [False] * n
        onstack = [False] * n
        count = [0] * n
        st = []
        
        cst = None
        def dfs(at):
            nonlocal cst
            visited[at] = True
            onstack[at] = True
            st.append(at)
            to = edges[at]
            
            if not visited[to]:
                dfs(to)
            else:
                if onstack[to]:
                    cst = to
            
            if cst is None:
                # print("no cycle", at)
                count[at] = count[to] + 1
                st.pop()
            elif cst == at:
                # print("cycle start", at)
                c = len(st) - st.index(at)
                while (p := st.pop()) != at:
                    count[p] = c
                count[at] = c
                cst = None
            # else:
            #     print("cycle", at, "start", cst)
                

            onstack[at] = False
        
            
        
        for at in range(n):
            if not visited[at]:
                cst = None
                dfs(at)
                # print(at, visited, onstack, st, count)

        return count