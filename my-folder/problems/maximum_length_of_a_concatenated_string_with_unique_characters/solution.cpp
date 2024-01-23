class Solution {
public:
    int maxLength(vector<string>& arr) {
        const int n = arr.size();
        std::vector<uint32_t> forb(n);
        std::vector<uint32_t> chars(n);

        for(int i=0; i<n; i++) {
            for (char c : arr[i]) {
                uint32_t bit = 1 << (c-'a');
                if (chars[i] & bit) {
                    forb[i] |= 1 << i;
                } else {
                    chars[i] |= bit;
                }
            }
        }

        for (int i=0; i<n; i++) {
            for (int j=i+1; j<n; j++) {
                if (chars[i] & chars[j]) {
                    forb[i] |= 1 << j;
                    forb[j] |= 1 << i;
                }
            }
            // std::cout << std::bitset<5>(forb[i]) << endl;
        }
        
        int ans = 0;
        for (int num=(1<<n) - 1; num >=0; --num) {
            bool valid = true;
            int total = 0;
            for (int i=0; i<n; i++) {
                if (num&(1 << i)) {
                    if (num&forb[i]) {
                        valid = false;
                        break;
                    }
                    total += arr[i].size();
                }
            }

            if (valid) {
                // std::cout << "valid num = " << num << endl;
                ans = std::max(ans, total);
            }
        }

        return ans;
    }
};