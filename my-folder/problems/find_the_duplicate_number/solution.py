class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        edge = nums
        slow = edge[0]
        fast = edge[edge[0]]
        # print(f"{slow}, {fast}")
        while slow != fast:
            slow = edge[slow]
            fast = edge[edge[fast]]
            # print(f"{slow}, {fast}")
        # print("Phase 2")        
        slow = 0
        # print(f"{slow}, {fast}")
        while slow != fast:
            slow = edge[slow]
            fast = edge[fast]
            # print(f"{slow}, {fast}")

        return fast

# 0 -> 1 -> 3 -> 2 -> 4
#                ^    |
#                +----+

# 0, 1, 2, 3, 4
# 3, 1, 3, 4, 2
#
# 0 -> 3 -> 4 -> 2
#      ^         |
#.     +---------+

# 0, 1, 2, 3, 4
# 1, 3, 4, 2, 1
#
# 0 -> 1 -> 3 -> 2 -> 4
#      ^              |
#.     +--------------+






