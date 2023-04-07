class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        while True:
            mid = (l+r) // 2
            if arr[mid-1] > arr[mid] > arr[mid+1]:
                r = mid
            elif arr[mid-1] < arr[mid] < arr[mid+1]:
                l = mid
            else:
                return mid
        