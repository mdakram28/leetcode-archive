class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        int n = arr.size();
        int mn=arr[0], mx=arr[0];
    
        for (int n: arr) {
            if (n<mn) mn=n;
            if (n>mx) mx=n;
        }
        if((mx-mn)%(n-1)) return false;

        int d = (mx-mn)/(n-1);
        if (d==0) return true;

        vector<bool> slots(mx-mn+1);
        

        for(int n: arr) {
            if((n-mn)%d || slots[n-mn]) return false;
            slots[n-mn] = true;
        }
        return true;
    }
};