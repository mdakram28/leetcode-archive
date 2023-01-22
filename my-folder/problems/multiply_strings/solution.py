
class Solution:
    def mult_dig(self, num, d, suffix):
        carry = 0
        ret = suffix[:]
        for d2 in num[::-1]:
            prod_d = d2 * d + carry
            ret.append(prod_d%10)
            carry = prod_d // 10
        if carry > 0:
            ret.append(carry)
        return ret

    def add(self, num1, num2):
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        carry = 0
        ret = []
        # print(f'{num1=}, {num2=}')
        for i in range(len(num2)):
            sum_d = num1[i] + num2[i] + carry
            ret.append(sum_d % 10)
            carry = sum_d // 10
            print(f'{sum_d=}')

        for i in range(len(num2), len(num1)):
            sum_d = num1[i] + carry
            ret.append(sum_d % 10)
            carry = sum_d // 10
            # print(f'{sum_d=}')
        if carry > 0:
            ret.append(carry)
        return ret

    def multiply(self, num1: str, num2: str) -> str:
        final = []
        suffix = []
        num1 = [int(d) for d in num1]
        num2 = [int(d) for d in num2]

        for d2 in num2[::-1]:
            prod = self.mult_dig(num1, d2, suffix)
            # print(f'{num1} x {d2} = {prod}')
            final = self.add(final, prod)
            # print(f'{final=}')
            suffix.append(0)
        
        return ''.join(map(str, final[::-1])).lstrip('0') or '0'