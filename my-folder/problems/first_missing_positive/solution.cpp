class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        bool hasVal[301];
        memset(hasVal, false, 301);
        
        for(int &n:nums) {
            if(n>=1 && n<=300) {
                hasVal[n] = true;
            }
        }
        
        for(int i=1;i<301;i++) {
            if(!hasVal[i]) return i;
        }
        return 301;
    }
};