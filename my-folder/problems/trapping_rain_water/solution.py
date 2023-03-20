class Solution:
    def trap(self, height: List[int]) -> int:
        last_max = height[0]
        last_max_i = 0
        trap = 0
        trap_total = 0

        for i in range(1, len(height)):
            val = height[i]
            if val >= last_max:
                last_max = val
                last_max_i = i
                trap_total += trap
                trap = 0
            else:
                trap += last_max - val
        
        right_max = height[-1]
        trap = 0
        for i in range(len(height)-2, last_max_i-1, -1):
            val = height[i]
            if val >= right_max:
                right_max = val
                trap_total += trap
                trap = 0
            else:
                trap += right_max - val
                # print()
        
        return trap_total
