class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        std::vector<std::vector<int>> answer(2);
        std::set<int> vals1(nums1.begin(), nums1.end());
        std::set<int> vals2(nums2.begin(), nums2.end());
        
        for (auto val: vals1) {
            if (!vals2.contains(val)) {
                answer[0].push_back(val);
            }
        }

        for (auto val: vals2) {
            if (!vals1.contains(val)) {
                answer[1].push_back(val);
            }
        }

        return answer;
    }
};