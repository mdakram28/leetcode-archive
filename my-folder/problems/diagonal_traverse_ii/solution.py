class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
            rows = deque()
            ans = []

            for r in range(len(nums)):
                rows.appendleft((r, 0))
                for _ in range(len(rows)):
                    row, c = rows.popleft()
                    ans.append(nums[row][c])
                    c += 1
                    if c < len(nums[row]):
                        rows.append((row, c))
            
            while rows:
                row, c = rows.popleft()
                ans.append(nums[row][c])
                c += 1
                if c < len(nums[row]):
                    rows.append((row, c))

            return ans