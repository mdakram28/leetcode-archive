units = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 
'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
tens = ['','','Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
hundred = 'Hundred'

powers = ["", "Thousand", "Million", "Billion", "Trillion"]

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        all_ret = []
        power = 0

        while num:
            ret = []
            n = num%1000
            num //= 1000

            if n >= 100:
                ret.append(units[n//100])
                ret.append(hundred)
                n = n%100
            if n >= 20:
                ret.append(tens[n//10])
                if n%10:
                    ret.append(units[n%10])
            elif n > 0:
                ret.append(units[n])
            
            if power and ret:
                ret.append(powers[power])
            power += 1
            
            all_ret = ret + all_ret
        
        return ' '.join(all_ret)
        
        
            
