class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        right = float('inf')
        left = float('inf')
        n = len(words)
        for i in range(n):
            if words[(startIndex+i)%n] == target:
                right = i
                break
        
        for i in range(n):
            if words[(startIndex-i)%n] == target:
                left = i
                break
        
        ret = min(left, right)
        
        return ret if ret != float('inf') else -1