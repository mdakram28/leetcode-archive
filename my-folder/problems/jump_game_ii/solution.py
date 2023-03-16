class Solution:
    def jump(self, nums: List[int]) -> int:
        UNREACHABLE = 100000
        jumps = [UNREACHABLE] * len(nums)
        jumps[0] = 0

        for i in range(0, len(nums)-1):
            if jumps[i] == UNREACHABLE:
                continue
            for j in range(i+1, min(i + nums[i] + 1, len(nums))):
                # print(f"Jumping from {i=} to {j=}")
                if jumps[j] > jumps[i] + 1:
                    jumps[j] = jumps[i] + 1
        
        # for i in range(1, len(nums)):
        #     min_jumps = -1
        #     for j in range(0, i):
        #         if (j + nums[j]) >= i and jumps[j] >= 0 and ((jumps[j] + 1) < min_jumps or min_jumps == -1):
        #             min_jumps = jumps[j] + 1
        #     jumps[i] = min_jumps

        return jumps[-1]
        