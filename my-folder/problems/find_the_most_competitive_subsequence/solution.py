class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        start = 0
        end = 0
        n = len(nums)
        st = Deque()
        ret = []

        rem = n-k
        while end < rem:
            while st and st[-1] > nums[end]:
                st.pop()
            st.append(nums[end])
            end += 1
        
        while end < n:
            while st and st[-1] > nums[end]:
                st.pop()
            st.append(nums[end])

            ret.append(st.popleft())
            
            end += 1
        
        return ret