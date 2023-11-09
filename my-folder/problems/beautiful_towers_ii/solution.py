class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        
        def get_totals(heights):
            # height, total, position
            st = [(-1, 0, -1)]

            totals = []
            for p, peak in enumerate(heights):
                while st[-1][0] >= peak:
                    st.pop()
                total = st[-1][1] + (p - st[-1][2])*peak
                st.append((peak, total, p))
                totals.append(total)
            return totals
        
        leftTotals = get_totals(maxHeights)
        rightTotals = get_totals(maxHeights[::-1])[::-1]
        
        # print("leftTotals", leftTotals)
        # print("rightTotals", rightTotals)
        
        ans = 0
        for p, peak in enumerate(maxHeights):
            ans = max(ans, leftTotals[p] + rightTotals[p] - peak)
        
        return ans