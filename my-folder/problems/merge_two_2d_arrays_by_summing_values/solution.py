class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        i = 0
        j = 0
        while i<len(nums1) and j < len(nums2):
            if nums1[i][0] < nums2[j][0]:
                ans.append(nums1[i])
                i += 1
            elif nums1[i][0] > nums2[j][0]:
                ans.append(nums2[j])
                j += 1
            else:
                nums1[i][1] += nums2[j][1]
                ans.append(nums1[i])
                i += 1
                j += 1
        ans.extend(nums1[i:])
        ans.extend(nums2[j:])
            
        return ans