class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        int n1 = str1.length(), n2 = str2.length();
        
        int limAns = min(n1, n2);
        
        for(int i=limAns; i>0; i--) {
            if (n1%i || n2%i) continue;
            bool matched = true;

            for(int j=0; j<n1 && matched; j++) {
                if (str1[j] != str1[j%i]) 
                    matched = false;
            }

            for(int j=0; j<n2 && matched; j++) {
                if (str2[j] != str1[j%i]) 
                    matched = false;
            }

            if (matched) return str1.substr(0, i);

        }
        return "";
    }
};