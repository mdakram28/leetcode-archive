class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = list(set(banned))
        banned.sort()
        bl = len(banned)
        b = 0
        
        count = 0
        total = 0
        for i in range(1, n+1):
            if b < bl and banned[b] == i:
                b += 1
                continue
            # print(i)
            if total + i > maxSum:
                break
            total += i
            count += 1
        
        return count