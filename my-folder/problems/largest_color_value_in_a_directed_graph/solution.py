from string import ascii_lowercase

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        num_parents = [0]*n
        graph = [[] for i in range(n)]
        on_stack = [False] * n
        freq = [0] * n

        for n1, n2 in edges:
            graph[n1].append(n2)
            num_parents[n2] += 1
        

        def has_cycle(at):
            if freq[at] == 1:
                return False
            if on_stack[at]:
                return True
            on_stack[at] = True
            for to in graph[at]:
                if has_cycle(to):
                    return True
            freq[at] = 1
            on_stack[at] = False
            return False


        def calc_freq(at, c):
            if freq[at] is not None:
                return freq[at]
                
            f = 0
            for to in graph[at]:
                f = max(f, calc_freq(to, c))
            
            if colors[at] == c:
                f += 1
            freq[at] = f
            return f
        
        for i in range(n):
            if has_cycle(i):
                return -1

        max_freq = -1
        for c in set(colors):
            for i in range(n):
                if num_parents[i] == 0:
                    freq = [None] * n
                    max_freq = max(max_freq, calc_freq(i, c))
        
        return max_freq

