class Solution {
    int numIndex[200001];
    
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        memset(numIndex, 0, sizeof(numIndex));
        
        for(int i=0; i<nums.size(); i++){
            numIndex[nums[i]+100000]++;
        }
        
        for(int i=0;i<nums.size();i++) {
            int n1 = nums[i];
            for(int j=i+1; j<nums.size(); j++) {
                int n2 = nums[j];
                if(n2 > -(n1/2.0)) break;
                
                int n3 = -(n1+n2);
                if((n3 + 100000) >= 200001) continue;
                int count = numIndex[n3 + 100000];
                // cout << "Count of " << n3 << " = " << count << endl;
                if(count > 0) {
                    if(n1 == n3) count--;
                    if(n2 == n3) count--;
                    if(count > 0) {
                        ans.push_back({n1, n2, n3});
                    } 
                }
                
                while(j<nums.size() && nums[j] == n2){
                    j++;
                }
                j--;
            }
            while(i<nums.size() && nums[i] == n1) {
                i++;
            }
            i--;
        }
        return ans;
    }
};