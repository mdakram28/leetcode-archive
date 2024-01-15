class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        int maxL = std::min(str1.length(), str2.length());
        for (int l=maxL; l>0; l--) {
            if (str1.length()%l != 0 || str2.length()%l != 0)
                continue;
            
            bool match = true;
            for(int j=l; j<str1.length(); j++) {
                if (str1[j] != str1[j%l]) {
                    match = false;
                    break;
                }
            }


            if (match) {
                for(int j=0; j<str2.length(); j++) {
                    // cout << l << ", " << j << endl;
                    if (str2[j] != str1[j%l]) {
                        match = false;
                        break;
                    }
                }
                if (match) return str1.substr(0, l);
            }

        }
        return "";
    }
};