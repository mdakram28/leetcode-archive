class Solution:
    def fractionToDecimal(self, num: int, den: int) -> str:
        ans = ""
        if (num < 0) != (den < 0):
            # print(num<0, den<0)
            if num != 0:
                ans = "-"

        if num < 0:
            num = -num
        if den < 0:
            den = -den

        ans += str(num//den)

        rem = num%den
        if rem == 0:
            return ans
        
        ans += '.'
        dig = []
        rem_ind = {}
        repeat = -1
        while rem > 0:
            if rem in rem_ind:
                repeat = rem_ind[rem]
                break
            rem_ind[rem] = len(dig)
            rem = rem*10
            dig.append(str(rem // den))
            rem = rem % den
        print(f"{dig=}")
        if repeat >= 0:
            
            ans += ''.join([*dig[:repeat], "(", *dig[repeat:], ")"])
        else:
            ans += ''.join(dig)
        
        return ans