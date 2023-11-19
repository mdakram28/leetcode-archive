class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if s1[0] != s2[0] or s1[0] != s3[0]: return -1
        count = 0
        for a,b,c in zip(s1, s2, s3):
            if a == b == c:
                count += 1
            else:
                break
        
        return len(s1)-count + len(s2)-count + len(s3)-count