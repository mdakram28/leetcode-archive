class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        r = bisect_left(arr, x)
        # if r == 0:
        #     return arr[:k]
        # if r >= len(arr):
        #     return arr[-k:]
        l = r-1
        arr.append(10000000)
        arr.append(-10000000)
        while r-l-1 < k:
            if x-arr[l] <= arr[r]-x:
                l -= 1
            else:
                r += 1
        print(l, r)
        return arr[l+1:r]

