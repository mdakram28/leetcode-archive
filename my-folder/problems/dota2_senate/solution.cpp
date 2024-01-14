class Solution {
public:
    string predictPartyVictory(string senate) {
        std::queue<int> r, d;
        int i = 0;

        for(char c: senate) {
            if (c=='R') r.push(i++);
            else d.push(i++);
        }
        
        while (r.size() > 0 && d.size() > 0) {
            if (r.front() < d.front()) {
                r.push(i++);
            } else {
                d.push(i++);
            }
            r.pop();
            d.pop();
        }

        constexpr auto R = "Radiant";
        constexpr auto D = "Dire";
        return r.size () > 0 ? R : D;
    }
};