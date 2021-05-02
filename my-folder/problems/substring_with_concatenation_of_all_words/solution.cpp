#define ll long long

#define A 54059 /* a prime */
#define B 76963 /* another prime */
#define C 86969 /* yet another prime */
#define FIRSTH 37 /* also prime */


class Solution {
    map<uint64_t, int> word_freq;
    map<uint64_t, list<int> *> word_pos;
    int word_len;
    int words_added = 0;
    int from_word;
    
    map<uint64_t, string> hash_to_word;
    
    uint64_t hash_str(const char* s)
    {
        uint64_t h = FIRSTH;
        int len = word_len;
        while (len) {
            len--;
            h = (h * A) ^ (s[len] * B);
        }
        return h; // or return h % C;
    }
    
    void print_word_freq(vector<string> &words) {
        map<string, bool> printed;
        for(string w: words) {
            uint64_t h = hash_str(w.c_str());
            int freq = word_freq[h];
            if(!printed[w]) {
                printf("%s : %lu = %d\n", w.c_str(), h, freq);
                printed[w] = true;
            }
        }
    }
    
    void print_word_pos() {
        for (auto it = word_pos.begin(); it != word_pos.end(); it++){
            if(it->second == NULL) continue;
            printf("\t%s : %lu = ", hash_to_word[it->first].c_str(), it->first);
            for(auto it2 = it->second->begin(); it2!=it->second->end(); it2++) {
                printf("%d, ", *it2);
            }
            printf("\n");
        }
    }
    
    void create_word_freq(vector<string> &words) {
        for(auto itr=words.begin();itr!=words.end();itr++) {
            word_freq[hash_str(itr->c_str())]++;
        }
    }

    void remove_all_words() {
        from_word += word_len*words_added;
        words_added = 0;
        for (auto it = word_pos.begin(); it != word_pos.end(); it++){
            if(it->second == NULL) continue;
            it->second->clear();
        }
    }

    void remove_word(string &s) {
        uint64_t to_rem = hash_str(&s.c_str()[from_word]);
        from_word += word_len;
        words_added--;
        list<int> *cwp = word_pos[to_rem];
        if(cwp != NULL) {
            cwp->pop_front();
        }
    }
    
    bool add_word(int pos, string &s) {
        uint64_t h = hash_str(&s.c_str()[pos]);
        list<int> *cwp = word_pos[h];
        int cwf = word_freq[h];
        
        if(!cwf) {
            remove_all_words();
            from_word += word_len;
            return false;
        }
        if(cwp == NULL) {
            cwp = new list<int>();
            word_pos[h] = cwp;
        }
        while(cwp->size() >= cwf) {
            // printf("\tRemoved 1 word\n");
            remove_word(s);
            // print_word_pos();
        }
        
        cwp->push_back(pos);
        words_added++;
        // printf("\tAdded\n");
        return true;
    }
    
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> ans;
        word_len = words[0].length();
        
        // for(string w: words) {
            // hash_to_word[hash_str(w.c_str())] = w;
        // }
        
        create_word_freq(words);
        // print_word_freq(words);
        
        for(int start=0;start<word_len;start++) {
            
            remove_all_words();
            from_word = start;
            // printf("Starting at %d\n", start);
            for(int to_word=start;to_word+word_len<=s.length();to_word+=word_len) {
                // printf("Adding to=%d   %.*s\n", to_word, word_len, s.c_str()+to_word);
                bool added = add_word(to_word, s);
                // print_word_pos();
                // printf("from=%d\n", from_word);
                if(words_added == words.size()) {
                    ans.push_back(from_word);
                }
            }
        }
        return ans;
    }
};