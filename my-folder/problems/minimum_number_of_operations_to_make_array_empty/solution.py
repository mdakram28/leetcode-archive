class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for count in Counter(nums).values():
            for op3 in range(count//3, max((count//3)-2, -1), -1):
                op2 = (count-op3*3)//2
                if op3*3 + op2*2 == count:
                    ans += op3+op2
                    break
            else:
                return -1
        
        return ans