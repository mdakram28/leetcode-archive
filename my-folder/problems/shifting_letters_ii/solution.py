class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        sh = [0] * (n+1)
        
        for start, end, d in shifts:
            d = d*2-1
            sh[start] += d
            sh[end+1] -= d
            
        ans = []
        total = 0
        for i in range(n):
            total += sh[i]
            ans.append(chr((ord(s[i]) - ord('a') + total) % 26 + ord('a')))
        
        return ''.join(ans)