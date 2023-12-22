class Solution {
public:
    int maxScore(string s) {
        int left = 0;
        int right = 0;
        int last = s.length()-1;
        for(int i=0; i<= last; i++)
        {
            if (s[i] == '1') right++;
        }

        int ans = 0;
        for(int i=0; i<last; i++)
        {
            if (s[i] == '0') left++;
            else right--;
            ans = std::max(ans, left+right);
        }
        return ans;
    }
};
