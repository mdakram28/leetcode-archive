class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def sorted_pos(t):
            ans = 0
            # closesy
            for i, row in enumerate(matrix):
                l = 0
                r = n
                while l<r:
                    mid = (l+r)//2
                    if row[mid] <= t:
                        l = mid+1
                    else:
                        r = mid
                # print(f"{i=}, {l=}")
                ans += l
            return ans


        lo = matrix[0][0]
        hi = matrix[-1][-1]
        # k -= 1
        # ans = hi
        while lo < hi:
            mid = (lo+hi)//2
            pos = sorted_pos(mid)
            # print(f"{lo=}, {hi=}, sorted_pos({mid})={pos}")
            if pos < k:
                lo = mid+1
            else:
                # ans = mid
                hi = mid

        return lo
