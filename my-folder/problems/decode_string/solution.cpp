class Solution {
    int parseInt(std::string &s, int &i) {
        int num = 0;
        while(s[i] >= '0' && s[i] <= '9') {
            num = num*10 + (s[i++]-'0');
        }
        return num;
    }

    int getClosing(std::string &s, int i) {
        int open = 1;
        i++;
        while (open > 0) {
            if (s[i] == '[') open++;
            else if (s[i] == ']') open--;
            i++;
        }
        return i-1;
    }

    void decode(std::string &s, int l, int r, std::string &res) {
        int i=l;
        while(i<r) {
            int count = parseInt(s, i);
            if (count == 0) count = 1;

            int start = res.size();
            if (s[i] == '[') {
                int closing = getClosing(s, i);
                decode(s, i+1, closing, res);
                i = closing+1;
            } else {
                res.push_back(s[i]);
                i++;
            }
            int end = res.size();

            res.resize(res.size() + (end-start)*(count-1));
            for(int j=1; j<count; j++) {
                memcpy(res.data() + start + (end-start)*j, res.data()+start, end-start);
            }
        }
    }
public:
    string decodeString(string s) {
        std::string ret;
        decode(s, 0, s.size(), ret);
        return ret;
    }
};