class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        a, ac = None, 0
        b, bc = None, 0
        for num in nums:
            # print(f"{a}:{ac}, {b}:{bc}, adding {num=}")
            if a == num:
                ac += 1
            elif b == num:
                bc += 1
            elif a is None:
                a = num
                ac = 1
            elif b is None:
                b = num
                bc = 1
            else:
                ac -= 1
                bc -= 1
                if ac == 0:
                    a, ac = None, 0
                if bc == 0:
                    b, bc = None, 0

        ans = set()
        if nums.count(a) > len(nums)//3:
            ans.add(a)
        
        if nums.count(b) > len(nums)//3:
            ans.add(b)
        
        return ans


