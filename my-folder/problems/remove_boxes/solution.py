class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        @cache
        def max_score(l, r, k):
            if l == r:
                return 0
            left_val = boxes[l]
            while l<r and boxes[l] == left_val:
                l += 1
                k += 1
            ans = k*k + max_score(l, r, 0)
            for mid in range(l+1, r):
                if boxes[mid] == left_val:
                    ans = max(
                        ans, 
                        max_score(l, mid, 0) + max_score(mid, r, k)
                    )
            return ans
        
        return max_score(0, n, 0)