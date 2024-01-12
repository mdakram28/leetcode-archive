class Solution {
public:
    bool halvesAreAlike(string s) {
        const int n = s.size();
        int a = 0;
        for(int i=0; i<n/2; i++) {
            char c = s[i];
            if (c >= 'a') c -= 32;
            switch(c) {
                case 'A':
                case 'E':
                case 'I':
                case 'O':
                case 'U':
                    a++;
            }
        }

        int b = 0;
        for(int i=n/2; i<n; i++) {
            char c = s[i];
            if (c >= 'a') c -= 32;
            switch(c) {
                case 'A':
                case 'E':
                case 'I':
                case 'O':
                case 'U':
                    b++;
            }
            if (b>a) return false;
        }

        return a==b;
    }
};