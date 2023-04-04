class Solution:
    def partitionString(self, s: str) -> int:
        f = collections.defaultdict(int)
        count = 0
        for i in range(len(s)):
            if f[s[i]] > 0:
                count += 1
                f.clear()

            f[s[i]] += 1
        
        return count + 1