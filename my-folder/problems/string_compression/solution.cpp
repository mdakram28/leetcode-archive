class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size();
        int j = 0;
        int count = 1;
        for(int i=1; i<=n; i++) {
            if (i==n || chars[i] != chars[i-1]) {
                chars[j++] = chars[i-1];
                if (count > 1) {
                    std::string s = std::to_string(count);
                    // printf("j = %d, s = %s\n", j, s.c_str());
                    memcpy(chars.data()+j, s.data(), s.length());
                    j += s.length();
                }
                count = 0;
            }
            count++;
        }
        return j;
    }
};