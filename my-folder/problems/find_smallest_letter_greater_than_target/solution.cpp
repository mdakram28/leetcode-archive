class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int l=0, r=letters.size();
        while(l<r) {
            int mid = (l+r)/2;
            if (letters[mid] <= target) {
                l = mid+1;
            } else {
                r = mid;
            }
        }
        return l<letters.size() ? letters[l] : letters[0];
    }
};