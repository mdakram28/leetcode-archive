class Solution {
public:
    string intToRoman(int num) {
        string ret = "";
        const string units[10] =      {"","I","II","III","VI","V","IV","IIV","IIIV","XI"};
        const string tens[10] =  {"","X","XX","XXX","LX","L","XL","XXL","XXXL","CX"};
        const string hundreds[10] = {"","C","CC","CCC","DC","D","CD","CCD","CCCD","MC"};
        
        
        int r = num%10;
        ret += units[r];
        num /= 10;
        
        r = num % 10;
        ret += tens[r];
        num /= 10;
        
        r = num % 10;
        ret += hundreds[r];
        num /= 10;
        
        while (num--) {
            ret += "M";
        }
        reverse(ret.begin(), ret.end());
        return ret;
    }
};