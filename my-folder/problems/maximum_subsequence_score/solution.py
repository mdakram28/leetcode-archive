class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        total = 0
        max_score = 0
        pq = []
        for n2, n1 in sorted(zip(nums2, nums1), reverse=True):
            if len(pq) == k:
                total -= heappop(pq)
            heappush(pq, n1)
            total += n1
            
            if len(pq) == k:
                max_score = max(max_score, total*n2)
        return max_score