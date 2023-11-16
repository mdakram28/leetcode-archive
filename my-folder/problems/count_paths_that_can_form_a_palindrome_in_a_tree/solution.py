class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        g = defaultdict(list)
        for i in range(1, len(parent)):
            g[parent[i]].append(i)
        
        allchars = set(s)
        count = defaultdict(int)
        total = 0
        prev = set()
        def dfs(at):
            nonlocal total
            
            if s[at] in prev:
                prev.remove(s[at])
            else:
                prev.add(s[at])
            path = ''.join(sorted(list(prev)))
            
            total += count[path]
            
            for c in allchars:
                if c in prev:
                    total += count[path.replace(c, '')]
                else:
                    total += count[''.join(sorted(path+c))]
            
            count[path] += 1
            
            for to in g[at]:
                dfs(to)
            
            if s[at] in prev:
                prev.remove(s[at])
            else:
                prev.add(s[at])
            
        
        dfs(0)
        return total