class Solution {
public:
    int myAtoi(string s) {
        int64_t ret = 0;
        int i = 0;
        int sign = 1;
        while(s[i] == ' ') {
            i++;
        }
        
        if(s[i] == '-') {
            sign = -1;
            i++;
        } else if (s[i] == '+'){
            sign = +1;
            i++;
        }
        
        while(s[i] >= '0' && s[i] <= '9') {
            ret = (ret*10) + (s[i]-'0');
            if (ret > INT_MAX) {
                return sign == -1 ? INT_MIN : INT_MAX;
            }
            i++;
        }
        
        ret *= sign;
        
        if (ret < INT_MIN) {
            return INT_MIN;
        } else if (ret > INT_MAX) {
            return INT_MAX;
        } else {
            return ret;
        }
        
    }
};