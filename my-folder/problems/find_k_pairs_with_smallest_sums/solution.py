class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        seen = set()
        nums1.append(float('inf'))
        nums2.append(float('inf'))

        heap = [(nums1[0]+nums2[0], 0, 0)]

        while len(seen) < k:
            a, i, j = heappop(heap)
            if a == float('inf'): break
            if (i, j) in seen: continue

            heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
            heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
            seen.add((i, j))
        
        return [(nums1[i], nums2[j]) for i, j in seen]
