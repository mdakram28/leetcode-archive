class Solution {
    public int characterReplacement(String s, int k) {
        int ans = 0;
        for (char c = 'A'; c<='Z'; c++) {
            int start = 0;
            int count = 0;
            for(int end = 0; end < s.length(); end++) {
                if (s.charAt(end) != c) {
                    count++;
                    while (start<s.length() && count > k) {
                        if (s.charAt(start) != c) count--;
                        start++;
                    }
                }
                // System.out.println(start + ", " + end);
                ans = Math.max(ans, end-start+1);
            }
        }
        return ans;
    }
}