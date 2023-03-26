from functools import cmp_to_key
from math import log10, floor

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # nums = list(map(str, nums))

        @cache
        def comp(a, b):
            mul = 1
            if len(b) > len(a):
                b, a = a, b
                mul = -1
            for i in range(len(b)):
                if a[i] < b[i]:
                    return 1*mul
                elif a[i] > b[i]:
                    return -1*mul
            j = 0
            for i in range(i, len(a)):
                if a[i] < a[j]:
                    return -1*mul
                elif a[i] > a[j]:
                    return 1*mul
                j += 1
            return 0

        @cache
        def comp2(a, b):
            if a == 0 and b == 0:
                return 0
            elif a == 0:
                return 1
            elif b == 0:
                return -1
            da = floor(log10(a))+1
            db = floor(log10(b))+1
            ab = a*(10**db) + b
            ba = b*(10**da) + a
            # print(f"compare {a=}, {b=}, {ab=}, {ba=}")
            if ab < ba:
                return 1
            elif ba < ab:
                return -1
            else:
                return 0
            
        nums.sort(key=cmp_to_key(comp2))
        print(nums)
        i = 0
        while i < len(nums)-1 and nums[i] == 0:
            i += 1
        return ''.join(map(str, nums[i:]))