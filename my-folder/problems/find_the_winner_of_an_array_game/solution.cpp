class Solution {
public:
    int getWinner(vector<int>& arr, int k) {
        int li = 0;
        int l = arr[0];
        const int s = arr.size();
        for(int i=1; i<s; i++)
        {
            if (arr[i] > l)
            {
                if((i-li-1) + (li == 0 ? 0 : 1)>= k)
                    return l;
                li = i;
                l = arr[i];
            }
        }
        return l;
    }
};

// 4, 7, 2, 1000
// 4, 2, 7, 1000
// 2, 4, 7, 1000