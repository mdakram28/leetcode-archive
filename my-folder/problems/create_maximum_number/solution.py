class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n1, n2 = len(nums1), len(nums2)
        ans = []

        dig1 = Deque()
        dig2 = Deque()
        merged = []
        # st = Deque()

        for c1 in range(max(0, k-n2), min(n1, k)+1):
            c2 = k-c1
            
            # Collect lex greatest numbers 
            for digs, nums, c in (dig1, nums1, c1), (dig2, nums2, c2):
                digs.append(99)
                for d in nums[:len(nums)-c]:
                    while d > digs[-1]:
                        digs.pop()
                    digs.append(d)
                l = 1
                for d in nums[len(nums)-c:]:
                    while len(digs) > l and d > digs[-1]:
                        digs.pop()
                    digs.append(d)
                    l += 1
                digs.popleft()
                while len(digs) > c:
                    digs.pop()
            
            # print(c1, c2)
            # print(dig1, dig2)
            # Merge the numbers
            merged.clear()
            while dig1 or dig2:
                merged.append(max(dig1, dig2).popleft())
            
            if merged > ans:
                ans = [*merged]
        
        return ans
