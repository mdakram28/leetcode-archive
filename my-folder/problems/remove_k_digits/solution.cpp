typedef pair<char, int> pi;

class Solution {
public:
    string removeKdigits(string num, int k) {
        string str;
        str.reserve(num.length()-k);
        priority_queue<pi, vector<pi>, greater<pi>> q;
        int end = num.length();
        
        
        int j=0;
        for(;j<k;j++) {
            q.push(make_pair(num[j], j));
        }
        int last_added = -1;
        while(j<end) {
            q.push(make_pair(num[j], j));
            while(q.top().second < last_added) {
                q.pop();
            }
            pair<char, int> to_add = q.top();
            q.pop();
            if (to_add.first != '0' || str.length() > 0) {
                str += to_add.first;
            }
            
            last_added = to_add.second;
            j++;
        }
        if (str.length() == 0) {
            return "0";
        } else {
            return str;
        }
    }
};