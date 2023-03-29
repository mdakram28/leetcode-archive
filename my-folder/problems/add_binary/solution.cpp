class Solution {
public:
    string addBinary(string a, string b) {
        vector<char> res;
        int i = a.length()-1, j = b.length()-1;
        bool carry = false;
        while (i>=0 && j>=0) {
            int s = (a[i--] == '1') + (b[j--] == '1') + carry;
            carry = s >> 1;
            if (s&1) {
                res.push_back('1');
            } else {
                res.push_back('0');
            }
        }
        while (i>=0) {
            int s = (a[i--] == '1') + carry;
            carry = s >> 1;
            res.push_back(s&1 ? '1' : '0');
        }
        while (j>=0) {
            int s = (b[j--] == '1') + carry;
            carry = s >> 1;
            res.push_back(s&1 ? '1' : '0');
        }
        if (carry) {
            res.push_back('1');
        }
        if (res.size()==0) {
            res.push_back('0');
        }
        return string(res.rbegin(), res.rend());
    }
};