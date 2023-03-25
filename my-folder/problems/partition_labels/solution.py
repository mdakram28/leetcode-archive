class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_pos = {}
        for i in range(len(s)):
            last_pos[s[i]] = i
        
        i = 0
        parts = []
        while i < len(s):
            start = i
            end = last_pos[s[i]]
            i += 1
            while i <= end:
                end = max(end, last_pos[s[i]])
                i += 1
            parts.append(i-start)
        
        return parts
