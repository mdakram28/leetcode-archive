class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        out = defaultdict(int)
        n = len(edges)+1
        graph = [[] for i in range(n)]
        
        guesses = set(map(tuple, guesses))
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        ch_away = {}
        def child_away(at, p):
            ans = 0
            for to in graph[at]:
                if to == p: continue
                ans += child_away(to, at) + int((at, to) in guesses)
            ch_away[at] = ans
            return ans
        
        par_away = {}
        def parent_away(at, p, away):
            par_away[at] = away
            for to in graph[at]:
                if to == p: continue
                parent_away(to, at, away + int((to, at) in guesses))
        
        def set_out(at, p, away):
            out[at] = ch_away[at] + par_away[at] + away
            for to in graph[at]:
                if to == p: continue
                set_out(to, at, away + ch_away[at] - ch_away[to] - int((at, to) in guesses))
        
        parent_away(0, None, 0)
        child_away(0, None)
        set_out(0, None, 0)
        
        # print(par_away)
        # print(ch_away)
        
        return sum(1 for f in out.values() if f>=k)
            
            
            
            
            
            