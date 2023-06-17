class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        print(arr1)
        print(arr2)

        @cache
        def min_op(i, j, lim):
            if i == -1: return 0
            ans = float('inf')
            if arr1[i] < lim:
                ans = min_op(i-1, j, arr1[i])
            
            l = 0
            h = j
            while l<h:
                mid = (l+h)//2
                if arr2[mid] < lim:
                    l = mid+1
                else:
                    h = mid
            
            if l > 0:
                ans = min(ans, min_op(i-1, l-1, arr2[l-1])+1)
            # print(i, j, lim, "=>", ans)
            return ans
        
        ret = min_op(len(arr1)-1, len(arr2), float('inf'))
        return ret if ret != float('inf') else -1
