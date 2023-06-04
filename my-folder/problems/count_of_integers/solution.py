class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        mod = 10**9 + 7
        
        @cache
        def count_all(i, prev):
            if i == 0:
                return 1 if (min_sum <= prev <= max_sum) else 0
            return sum(count_all(i-1, prev+dig) for dig in range(10))
        
        @cache
        def count_nums2(i, prev):
            if i == 0: 
                return 1 if (min_sum <= prev <= max_sum) else 0
            
            ans = sum(count_all(i-1, prev+dig) for dig in range(int(num2[-i]))) + count_nums2(i-1, prev+int(num2[-i]))
            # print(i, lim, prev, ans)
            return ans%mod
        
        @cache
        def count_nums1(i, prev):
            if i == 0: 
                return 1 if (min_sum <= prev <= max_sum) else 0
            
            ans = sum(count_all(i-1, prev+dig) for dig in range(int(num1[-i]))) + count_nums1(i-1, prev+int(num1[-i]))
            # print("nums1", i, lim, prev, ans)
            return ans%mod
        
        ans = count_nums2(len(num2), 0) - count_nums1(len(num1), 0)
        if min_sum <= sum(int(d) for d in num1) <= max_sum:
            # print("NUM1 INCLUDED")
            ans += 1
        
        return ans%mod
        
        