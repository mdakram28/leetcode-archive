class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ng = {}
        st = []
        for i in range(len(nums2)-1, -1, -1):
            val = nums2[i]
            # ind[val] = i
            while st and st[-1] < val:
                st.pop()
            if st:
                ng[val] = st[-1]
            else:
                ng[val] = -1
            st.append(val)
        
        return [ng[n] for n in nums1]