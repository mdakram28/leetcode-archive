class Solution:
    def maximumLength(self, s: str) -> int:
        f = defaultdict(list)
        
        s += "$"
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                f[s[i-1]].append(count)
                count = 1
        
        ans = 0
        for counts in f.values():
            counts.sort(reverse=True)
            c = len(counts)
            for i, l in enumerate(counts):
                if i+1 < c and counts[i+1] >= l and i+2 < c and counts[i+2] >= l:
                    ans = max(ans, l)
                elif i+1 < c and counts[i+1] >= l-1:
                    ans = max(ans, l-1)
                else:
                    ans = max(ans, l-2)
        
        return ans if ans > 0 else -1