class Solution {
    bool isInteger(string &s, int start, int end) {
        bool hasSign = false;
        for(int i=start; i<end; i++) {
            char ch = s[i];
            if (ch == '+' || ch == '-') {
                if (i != start) return false;
                hasSign = true;
            } else if (ch == '.') {
                return false;
            }
        }
        int l = end-start;
        return l>=2 || (l==1 && !hasSign);
    }
    
    bool isDecimalInteger(string &s, int start, int end) {
        int dig_count = 0;
        int dot_count = 0;
        for(int i=start; i<end; i++) {
            char ch = s[i];
            if (ch == '+' || ch == '-') {
                if (i != start) return false;
            } else if (ch == '.') {
                dot_count++;
            } else {
                dig_count++;
            }
        }
        
        return dot_count <= 1 && dig_count >= 1;
    }
public:
    bool isNumber(string s) {
        int e_index = -1;
        int e_count = 0;

        int l = s.length();
        
        for(int i=0;i<l;i++) {
            char ch = s[i];
            if (ch == '.') {
                
            } else if (ch == 'e' || ch == 'E') {
                e_index = i;
                e_count++;
            } else if (ch == '+' || ch == '-') {
                
            } else if (ch < '0' || ch > '9') {
                return false;
            }
        }
        if (e_count > 1) {
            return false;
        } else if (e_count == 1) {
            return isDecimalInteger(s, 0, e_index) && isInteger(s, e_index+1, l);
        } else {
            return isDecimalInteger(s, 0, l);
        }
    }
};