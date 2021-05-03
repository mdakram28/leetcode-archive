class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        auto i1 = nums1.begin();
        auto i2 = nums2.begin();
        
        int n1 = nums1.size();
        int n2 = nums2.size();
        int mi1,mi2;
        if((n1+n2)%2 == 0) {
            mi1 = (n1+n2-2)/2;
            mi2 = (n1+n2)/2;
        } else {
            mi1 = (n1+n2-1)/2;
            mi2 = mi1;
        }
        
        // printf("%d,%d\n", mi1, mi2);
        
        int c1=0, c2=0;
        int median = 0;
        while(i1!=nums1.end() || i2!=nums2.end()) {
            if((i1 != nums1.end() ? *i1 : INT_MAX) <= (i2 != nums2.end() ? *i2 : INT_MAX)) {
                if((c1+c2) == mi1 || (c1+c2) == mi2) {
                    median+=*i1;
                }
                i1++;
                c1++;
            } else {
                if((c1+c2) == mi1 || (c1+c2) == mi2) {
                    median+=*i2;
                }
                i2++;
                c2++;
            }
        }
        
        return (n1+n2)%2==0 ? median/2.0 : median;
    }
};