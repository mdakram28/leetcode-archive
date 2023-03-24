class Solution {
public:
    int getSum(int a, int b) {
        int sum = 0;
        uint32_t carry = 0;
        uint32_t mask = 1;
        while (mask) {
            int x = a & mask;
            int y = b & mask;
            sum |= x ^ y ^ carry;
            carry = x&y | x&carry | y&carry;

            carry <<= 1;
            mask <<= 1;

        }
        

        return sum;
    }
};