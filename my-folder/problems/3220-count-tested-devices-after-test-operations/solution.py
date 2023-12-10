class Solution:
    def countTestedDevices(self, B: List[int]) -> int:
        ans = 0
        for i in range(len(B)):
            if B[i] == 0: continue
            ans += 1
            for j in range(i+1, len(B)):
                if B[j] > 0:
                    B[j] -= 1
        
        return ans
