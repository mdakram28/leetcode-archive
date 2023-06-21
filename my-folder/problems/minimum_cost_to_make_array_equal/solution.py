class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        arr = sorted(zip(nums, costs))

        n = len(nums)
        cost = sum(abs(val-arr[0][0])*c for val,c in arr)
        ans = cost

        left = arr[0][1]
        total_cost = sum(costs)

        for i in range(1, n):
            cost += (2*left-total_cost)*(arr[i][0]-arr[i-1][0])

            ans = min(ans, cost)

            left += arr[i][1]
            # right -= arr[i][1]

        return ans
