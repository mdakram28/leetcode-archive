#define llu unsigned long long
class Solution {
    
public:
    int numDecodings(string s) {
        char charMap[] = {10,-1,-1,-1,-1,-1,0,1,2,3,4,5,6,7,8,9};
        int n1_map[] = {0,1,1,1,1,1,1,1,1,1,9};
        int n2_map[11][11] = {
            {0,1,1,0,0,0,0,0,0,0,2},
            {0,1,1,0,0,0,0,0,0,0,2},
            {0,1,1,0,0,0,0,0,0,0,2},
            {0,1,1,0,0,0,0,0,0,0,2},
            {0,1,1,0,0,0,0,0,0,0,2},
            {0,1,1,0,0,0,0,0,0,0,2},
            {0,1,1,0,0,0,0,0,0,0,2},
            {0,1,0,0,0,0,0,0,0,0,1},
            {0,1,0,0,0,0,0,0,0,0,1},
            {0,1,0,0,0,0,0,0,0,0,1},
            {0,9,6,0,0,0,0,0,0,0,15}
        };
        
        char lsx = s[0];
        char sx;
        llu total_ways_last = 1;
        llu total_ways = n1_map[charMap[lsx-'*']];
        
        for(auto i=s.begin()+1;i!=s.end();i++) {
            char lsx = *(i-1);
            char sx = *i;
            
            // int n1 = 1;
            // if(sx == '0') n1 = 0;
            // else if(sx == '*') n1 = 9;
            
            
            // int n2 = 0;
            // if(lsx == '0') n2 = 0;
            // else if(lsx == '1') n2 = sx == '*' ? 9 : 1;
            // else if(lsx == '2') n2 = sx == '*' ? 6 : (sx=='7' || sx=='8' || sx=='9' ? 0 : 1);
            // else if(lsx == '*') {
            //     n2 = 2;
            //     if(sx == '7' || sx=='8' || sx=='9') n2 = 1;
            //     else if(sx == '*') n2 = 15;
            // }
            
            int n1 = n1_map[charMap[sx-'*']];
            int n2 = n2_map[charMap[sx-'*']][charMap[lsx-'*']];
            
            llu temp = total_ways;
            total_ways = (total_ways*n1 + total_ways_last*n2)%1000000007;
            total_ways_last = temp;
            // cout << total_ways << endl;
        }
        return total_ways;
    }
};