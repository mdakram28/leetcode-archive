class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            # print(stack, [height[i] for i in stack])
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
                # print(f"{h=}, {w=}")
            stack.append(i)
        # height.pop()
        return ans